import pytest

from unittest import mock

from usagovjobs import constants

@pytest.fixture(autouse=True)
def mock_constants(monkeypatch):
    monkeypatch.setattr("usagovjobs.main.constants.BASE_URL", "test-url-")
    monkeypatch.setattr(constants, name="USA_JOBS_API_KEY", value="test-key")
    monkeypatch.setattr(constants, name="USA_JOBS_USER_AGENT", value="test-user-agent")
    monkeypatch.setattr(constants, name="HOST", value="test-host")


@pytest.fixture(scope="function")
def headers():
    return {
        "Host": constants.HOST,
        "User-Agent": constants.USA_JOBS_USER_AGENT,
        "Authorization-Key": constants.USA_JOBS_API_KEY
    }

@pytest.fixture(scope="function")
def mock_request_object(mock_response_object):    
    class Mock_Requests:
       
        def get(self, url, headers, params):
            return mock_response_object
        
    return Mock_Requests()

@pytest.fixture(scope="function")
def mock_response_object():
    class Mock_Response:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            
        def json(self):
            return self.json_data
        
        def status(self):
            return self.status_code
        
    return Mock_Response(json_data={"test":"data"}, status_code=200)