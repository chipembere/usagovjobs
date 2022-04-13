import os
import csv
import json
import sqlite3
import smtplib
import requests
import sqlalchemy
from os import environ
from datetime import date
from typing import List
from sqlalchemy import create_engine
from pydantic import BaseModel

from usagovjobs import constants


def db_connect(db_name: str):
    """Connects to database and returns a database connection object."""
    engine = create_engine(f"sqlite:///{db_name}.db", echo=True, future=True)
    return engine


def get_api_call(
    endpoint: str,
    params: dict,
    base_url: str = constants.BASE_URL,
    page_limit: int = constants.PAGE_LIMIT,
):
    """
    Makes a GET request with appropriate parameters, authentication,
    while respecting page and rate limits, and paginating if needed.

    Returns a JSON API response object."""
    headers = {
        "Host": constants.HOST,
        "User-Agent": constants.USA_JOBS_USER_AGENT,
        "Authorization-Key": constants.USA_JOBS_API_KEY,
    }
    url = f"{base_url}{endpoint}"
    try:
        resp = requests.get(url=url, headers=headers, params=params)
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def extract_positions(titles: List[str], keywords: List[str]):
    """
    Makes API calls for titles and keywords, parses the responses.

    Returns the values ready to be loaded into database."""
    keywords_responses = []
    titles_response = get_api_call(
        endpoint="search",
        params={"Page": 1, "ResultsPerPage": 500, "PositionTitle": titles},
    )
    for keyword in keywords:
        keywords_responses.append(
            get_api_call(
                endpoint="search",
                params={"Page": 1, "ResultsPerPage": 500, "Keywords": keyword},
            )
        )

class Position(BaseModel):
    position_id: str
    position_title: str
    organization_name: str
    min_salary: float
    max_salary: float
    salary_interval: str
    who_may_apply: str

def parse_positions(response_json):
    """
    Parses a response JSON for wanted fields.

    Returns a list of positions of appropriate object type."""
    parsed_positions = []
    for position in response_json["SearchResult"]["SearchResultItems"]:
        position_data = position["MatchedObjectDescriptor"]
        parsed_positions.append(
            Position(
                position_id=position_data["PositionID"],
                position_title=position_data["PositionTitle"],
                organization_name=position_data["OrganizationName"],
                min_salary=position_data["PositionRemuneration"][0]["MinimumRange"],
                max_salary=position_data["PositionRemuneration"][0]["MaximumRange"],
                salary_interval=position_data["PositionRemuneration"][0]["RateIntervalCode"],
                who_may_apply="United States Citizens " if position_data["UserArea"]["Details"]["WhoMayApply"]["Name"] == "" else position_data["UserArea"]["Details"]["WhoMayApply"],
            )
        )
    return parsed_positions

def prep_database(db_name: str):
    """Connects to database and creates tables if necessary."""


def load_data(row_values: List[dict], table_name: str):
    """Connects to database and loads values in corresponding tables."""


def run_analysis(output_path: str):
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


def send_reports(recipient_email: str, reports_path: str):
    """
    Loops through present CSV files in reports_path,
    and sends them via email to recipient.

    Returns None
    """
    pass


if __name__ == "__main__":
    """
    Puts it all together, and runs everything end-to-end.

    Feel free to create additional functions that represent distinct functional units,
    rather than putting it all in here.

    Optionally, enable running this script as a CLI tool with arguments for position titles and keywords.
    """
    # import argparse
