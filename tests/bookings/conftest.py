import pytest
from utils.routes import Routes
from utils.api_client import BaseSession
from utils.test_cases import TestCases

@pytest.fixture(scope="session")
def booking_client(Base_session : BaseSession):
    Base_session.end_point(Routes.booking)
    return Base_session

@pytest.fixture(scope="function")
def booked_data_fixture():
    """Fixture to generate test data for duplicate booking test at runtime (not collection time)."""
    return TestCases.booked_data()

@pytest.fixture(scope="function")
def deleted_id_for_delete_test():
    """Fixture to generate deleted ID for test_delete_deletedBooking at runtime."""
    return TestCases.deleted0()

@pytest.fixture(scope="function")
def deleted_id_for_get_test():
    """Fixture to generate deleted ID for test_get_deleted_booking at runtime."""
    return TestCases.deleted1()