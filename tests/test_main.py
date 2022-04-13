import pytest
import requests
import sqlalchemy

from unittest import mock
from pydantic import BaseModel

from usagovjobs import main, constants


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
    assert res[0].position_title == "COMPUTER SCIENTIST (DATA SCIENTIST/DATA ANALYST)"
    assert res[0].min_salary == 97738.0
    assert res[0].who_may_apply == "United States Citizens "


@mock.patch("usagovjobs.main.get_api_call")
def test_extract_and_parse_positions(mock_get_api_call, response_json):
    mock_get_api_call.return_value = response_json
    res = main.extract_positions(titles=["Data Engineer"], keywords=["data"])
    assert mock_get_api_call.call_count == 2
    # import pdb; pdb.set_trace()
    assert res[1].position_title == "Data Scientist"
    assert res[1].min_salary == 126233.0
    assert res[1].who_may_apply == "United States Citizens "


def test_prep_database():
    """Connects to database and creates tables if necessary."""


def test_load_data():
    """Connects to database and loads values in corresponding tables."""


def test_run_analysis():
    """
    Runs 3 SQL queries to obtain results that could answer the following questions:
    1. How do *monthly* starting salaries differ across positions with different titles and keywords?
    2. Do (filtered) positions for which 'United States Citizens' can apply have a higher average salary than those
       that 'Student/Internship Program Eligibles' can apply for? (by month)
    3. What are the organisations that have most open (filtered) positions?

    Exports results of queries into CSV files in the `output_path` directory.

    ** Feel free to break this function down into smaller units
    (hint: potentially have a `export_csv(query_result)` function)
    """
    pass


def test_send_reports():
    """
    Loops through present CSV files in reports_path,
    and sends them via email to recipient.

    Returns None
    """
    pass
