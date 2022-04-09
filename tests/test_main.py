from usagovjobs import main


def test_db_connect():
    """Connects to database and returns a database connection object. """
    # test_db_connect()
    pass

def test_get_api_call():
    """
    Makes a GET request with appropriate parameters, authentication,
    while respecting page and rate limits, and paginating if needed. 
    
    Returns a JSON API response object. """
    pass

def test_extract_positions():
    """
    Makes API calls for titles and keywords, parses the responses. 
    
    Returns the values ready to be loaded into database. """
    pass

def test_parse_positions():
    """
    Parses a response JSON for wanted fields. 

    Returns a list of positions of appropriate object type. """
    pass

def test_prep_database():
    """Connects to database and creates tables if necessary. """

def test_load_data():
    """Connects to database and loads values in corresponding tables. """

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