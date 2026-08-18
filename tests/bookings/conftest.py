import pytest
from utils.routes import Routes
from utils.api_client import BaseSession
@pytest.fixture(scope="session")
def booking_client(Base_session : BaseSession):
    Base_session.end_point(Routes.booking)
    return Base_session