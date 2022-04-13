# usagovjobs
Search gov data jobs and store the results in a local db for downstream use (report email).

## .env file
You'll need these values in a .env file in the root directory.

BASE_URL=https://data.usajobs.gov/api/
DB_NAME=<database name>
USA_JOBS_API_KEY=<api key>
USA_JOBS_USER_AGENT=<user agent>
HOST=data.usajobs.gov

## tests
To run tests
`make test`
