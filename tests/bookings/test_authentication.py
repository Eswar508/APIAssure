import pytest
from testing_services.execute import Execute_with_data
from utils.test_cases import TestCases
import allure
from utils.api_client import BaseSession
@allure.epic("Authentication")
@allure.feature("authenticate valid token")
@pytest.mark.parametrize("test_case",TestCases.auth_post())
def test_auth_booking(booking_client:BaseSession,test_case:dict):
    allure.dynamic.title(f"posting with {"in" if  test_case["header"] else ""}valid token")
    allure.dynamic.description(f"posting data with {"in" if  test_case["header"] else ""}valid token and check the response against expected ")
    allure.severity(allure.severity_level.CRITICAL)
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,test_case["data"],test_case["expected_code"])
    with allure.step("validating response for token authentication"):
        exe.auth_post_test(test_case["header"])
@allure.epic("Authentication")
@allure.feature("authenticate valid token")
@pytest.mark.parametrize("test_case",TestCases.auth_put())
def test_unauthorized_edit(booking_client:BaseSession,test_case:dict):
    allure.dynamic.title(f"updating with {"in" if  test_case["header"] else ""}valid token")
    allure.dynamic.description(f"updating data with {"in" if  test_case["header"] else ""}valid token and check the response against expected ")
    allure.dynamic.severity(allure.severity_level.NORMAL)
    load=TestCases.put_data()
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,load,test_case["expected_code"],test_case["id"])
    with allure.step("validating response for token authentication"):
        exe.auth_edit_test(test_case["header"])