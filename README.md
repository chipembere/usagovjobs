# usagovjobs
Search gov data jobs and store the results in a local db for downstream use (report email).

## .env file
You'll need the values below in a .env file in the root directory.

BASE_URL=https://data.usajobs.gov/api/\
DB_NAME=<database name>\
USA_JOBS_API_KEY=<api key>\
USA_JOBS_USER_AGENT=<user agent>\
HOST=data.usajobs.gov

## running locally
[Install poetry on your device](https://python-poetry.org/docs/)
`poetry shell`
`poetry install`
`poetry run python usagovjobs/main.py -r`

## tests
To run tests
`poetry shell`
`poetry install`
`make test`
