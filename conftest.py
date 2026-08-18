import pytest
from utils.api_client import BaseSession
import requests
from utils.routes import Routes
from utils.helper import get_token
from utils.data_loader import data_loader
@pytest.fixture(scope='session')
def Base_session():
    session=requests.Session()
    session.headers.update({'Content-Type': 'application/json',
                            'Accept': 'application/json'})
    s=BaseSession(session, Routes.base_url)
    s.end_point(Routes.login)
    response=s.generate_token(data_loader("test_data/login/data.json"))
    token=get_token(response)
    s.set_token(token)
    return s
