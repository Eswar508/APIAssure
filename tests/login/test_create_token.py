import pytest
from utils.assertions import Validate
from utils.test_cases import TestCases
import allure
from utils.api_client import BaseSession
@allure.epic("Authentication")
@allure.feature("Generate Token")
@pytest.mark.smoke
@pytest.mark.authentication
def test_generate_token(auth_client:BaseSession):
    data=TestCases.login()
    allure.dynamic.title(f"Testing with {data['username']}")
    allure.dynamic.description(f"testing with valid user name {data['username']} whose results to be expected with status code 200 and token in json body as any string")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    with allure.step("obtaining token"):
        response=auth_client.generate_token(data)
        assert_True=Validate(response)
    with allure.step("checking status code"):
        assert_True.assert_status_code(200)
    with allure.step("checking is it string"):
        assert_True.assert_token_is_string()        
@allure.epic("Authentication")
@allure.feature("Generate Token")
@pytest.mark.regression
@pytest.mark.authentication
@pytest.mark.parametrize("test_case",TestCases.invalid_login())
def test_generate_token_with_invalid_data(auth_client:BaseSession,test_case:dict):
    allure.dynamic.title(f"Testing with {test_case['username']}")
    allure.dynamic.description(f"testing with invalid user name {test_case['username']} whose results to be expected with status code 200 and absense of token in json body")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    with allure.step("obtaining token"):
        response=auth_client.generate_token(test_case)
        assert_True=Validate(response)
    with allure.step("checking status code"):
        assert_True.assert_status_code(200)
    with allure.step("checking absence of token"):
        assert_True.assert_token_not_present()