import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
PAGE_LIMIT = 500
DB_NAME = os.getenv('DB_NAME')
USA_JOBS_API_KEY = os.getenv('USA_JOBS_API_KEY')
USA_JOBS_USER_AGENT = os.getenv('USA_JOBS_USER_AGENT')
HOST = os.getenv('HOST')