import os
import requests
import sqlalchemy

from unittest import mock
from sqlalchemy import select

from usagovjobs import main, constants, models


def test_db_connect():
    """Connects to database and returns a database connection object."""
    assert type(main.db_connect(db_name=constants.DB_NAME)) == sqlalchemy.future.Engine


@mock.patch("usagovjobs.main.requests")
def test_get_api_call_args(mock_get, mock_request_object, headers):
    params = {"Page": 1, "ResultsPerPage": 500, "Keywords": "data"}
    mock_get.return_value = mock.MagicMock(return_value=mock_request_object)
    main.get_api_call(endpoint="search", params=params, base_url=constants.BASE_URL)

    mock_get.get.assert_called_with(
        url=constants.BASE_URL + "search", headers=headers, params=params
    )


@mock.patch("usagovjobs.main.requests.get")
def test_get_api_call_response(mock_get, mock_response_object, headers):
    params = {"Page": 1, "ResultsPerPage": 500, "Keywords": "data"}
    mock_get.return_value = mock_response_object
    resp = main.get_api_call(
        endpoint="search", params=params, base_url=constants.BASE_URL
    )
    assert resp == mock_response_object.json_data


@mock.patch("usagovjobs.main.get_api_call")
def test_extract_positions(mock_get_api_call):
    mock_get_api_call.return_value = mock.MagicMock()
    main.extract_positions(titles=["Data Engineer"], keywords=["data"])
    assert mock_get_api_call.call_count == 2


def test_parse_positions(response_json):
    res = main.parse_positions(response_json)
    assert type(res) == list
    assert (
        res[0]["position_title"] == "COMPUTER SCIENTIST (DATA SCIENTIST/DATA ANALYST)"
    )
    assert res[0]["min_salary"] == 97738.0
    assert res[0]["who_may_apply"] == "United States Citizens "


@mock.patch("usagovjobs.main.get_api_call")
def test_extract_and_parse_positions(mock_get_api_call, response_json):
    mock_get_api_call.return_value = response_json
    res = main.extract_positions(titles=["Data Engineer"], keywords=["data"])
    assert mock_get_api_call.call_count == 2
    assert res["data_engineer"][1]["position_title"] == "Data Scientist"
    assert res["data_engineer"][1]["min_salary"] == 126233.0
    assert res["data_engineer"][1]["who_may_apply"] == "United States Citizens "


@mock.patch("usagovjobs.main.db_connect")
def test_prep_database(mock_db_connect):
    mock_db_connect.return_value = mock.MagicMock()
    main.prep_database(db_name="test_db")
    mock_db_connect.assert_called_once_with(db_name="test_db")


@mock.patch("usagovjobs.main.db_connect")
@mock.patch("usagovjobs.main.get_api_call")
def test_load_data(mock_get_api_call, mock_prep_database, mock_db, response_json):
    mock_prep_database.return_value = mock_db
    mock_get_api_call.return_value = response_json
    res = main.extract_positions(titles=["Data Engineer"], keywords=["data"])
    main.load_data(table_name="data_engineer", row_values=res["data_engineer"])
    s = select(models.Base.metadata.tables["data_engineer"])
    conn = mock_db.connect()
    result = conn.execute(s)
    assert result.fetchone()


@mock.patch("usagovjobs.main.prep_database")
@mock.patch("usagovjobs.main.get_api_call")
def test_run_analysis(mock_get_api_call, mock_prep_database, mock_db, response_json):
    mock_prep_database.return_value = mock_db
    mock_get_api_call.return_value = response_json
    res = main.extract_positions(titles=["Data Engineer"], keywords=["data"])
    main.load_data(table_name="data_engineer", row_values=res["data_engineer"])
    main.load_data(table_name="data_scientist", row_values=res["data"])
    main.load_data(table_name="data_analyst", row_values=res["data"])
    main.load_data(table_name="data", row_values=res["data"])
    main.load_data(table_name="analysis", row_values=res["data"])
    main.load_data(table_name="analytics", row_values=res["data"])
    res = main.run_analysis(output_path="test_dir")
    assert os.path.exists("test_dir/q1_salary_report.csv")


def test_send_reports():
    """
    Loops through present CSV files in reports_path,
    and sends them via email to recipient.

    Returns None
    """
    pass
