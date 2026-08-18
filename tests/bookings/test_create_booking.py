import pytest
from utils.test_cases import TestCases
from testing_services.execute import Execute_with_data
import allure
from utils.api_client import BaseSession
@allure.epic("posting data")
@allure.feature("valid input formate")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.create_booking 
@pytest.mark.parametrize("test_case",TestCases.booking())
def test_valid_data(booking_client:BaseSession,test_case:dict):
    allure.dynamic.title(f"testing valid input {test_case["firstname"]}")
    allure.dynamic.description("checking 200 status code and  json containing posted data of response for posting valid input data")
    allure.severity(allure.severity_level.BLOCKER)
    with allure.step("saving data"):
        exe=Execute_with_data(booking_client,data=test_case,code=200)
    with allure.step("validating response for valid data"):
        exe.post_response_Test()
@allure.epic("posting data")
@allure.feature("invalid input formate")
@pytest.mark.regression
@pytest.mark.create_booking
@pytest.mark.parametrize(("title","test_case"),TestCases.invalid_booking().items())
def test_invalid_data(booking_client:BaseSession,test_case:dict,title:str):
    allure.dynamic.title(f"testing invalid input {title}")
    allure.dynamic.description("checking 500 status code and  json containing error message of response for posting invalid input data")
    allure.severity(allure.severity_level.CRITICAL)
    with allure.step("saving data"):
        exe=Execute_with_data(booking_client,data=test_case,code=500)
    with allure.step("validating response for invalid data"):
        exe.post_response_Test()
@allure.epic("posting data")
@allure.feature("valid input formate")
@pytest.mark.create_booking
def test_duplicate_booking(booking_client:BaseSession,data=TestCases.booked_data()):
    allure.dynamic.title(f"booking booked input {data["firstname"]}")
    allure.dynamic.description("checking 422 status code and  json containing error message of response for posting valid input data but duplicate")
    pytest.exit("NO id's with valid booking data from post response so cannot proceed to further methods") if data is None else None
    with allure.step("saving data"):
        exe=Execute_with_data(booking_client,data=data,code=422)
    with allure.step("validating response for duplicate valid data"):
        exe.post_response_Test()