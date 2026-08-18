import pytest
from utils.api_client import BaseSession
from utils.routes import Routes
@pytest.fixture(scope='session')
def auth_client(Base_session:BaseSession):
    Base_session.end_point(Routes.login)
    return Base_session