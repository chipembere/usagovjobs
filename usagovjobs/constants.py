import os
from dotenv import load_dotenv

#
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
PAGE_LIMIT = 500
DB_NAME = os.getenv("DB_NAME")
USA_JOBS_API_KEY = os.getenv("USA_JOBS_API_KEY")
USA_JOBS_USER_AGENT = os.getenv("USA_JOBS_USER_AGENT")
HOST = os.getenv("HOST")
KEYWORD_TABLE_MAP = {
    "Data Analyst": "data_analyst",
    "Data Scientist": "data_scientist",
    "Data Engineer": "data_engineer",
    "data": "data",
    "analysis": "analysis",
    "analytics": "analytics",
}
POSITION_TITLES = ["Data Scientist", "Data Engineer", "Data Analyst"]
KEYWORDS = ["data", "analysis", "analytics"]
OUTPUT_PATH = "reports"
EMAIL_RECEPIENT = "recepient@email.com"
