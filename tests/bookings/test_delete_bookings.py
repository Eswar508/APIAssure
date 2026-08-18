import pytest
from testing_services.execute import Execute_with_data
from utils.test_cases import TestCases
import allure
from utils.api_client import BaseSession
@allure.epic("delete")
@allure.feature("correct id")
@allure.story("delete valid id")
@pytest.mark.delete_booking
@pytest.mark.parametrize("id",TestCases.delete())
def test_delete_booking(booking_client:BaseSession,id:int):
    allure.dynamic.title(f"delete id {id}")
    allure.dynamic.description(f"deleting the id {id} to check if the status code is 201 and a json message confirming the id is deleted")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=201,id=id)
    with allure.step("validating response of delete method against expected"):
        exe.delete_response_Test()
@allure.epic("delete")
@allure.feature("incorrect id")
@allure.story("delete non existent id")
@pytest.mark.delete_booking
def test_delete_non_existent_booking(booking_client:BaseSession):
    id=999999
    allure.dynamic.title(f"try to delete non existent id {id}")
    allure.dynamic.description(f"trying to delete non existent id {id} to check if the status code is 405 and a json message confirming that deleting failed")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=405,id=id)
    with allure.step("validating response"):
        exe.delete_response_Test()
@allure.epic("delete")
@allure.feature("incorrect id")
@allure.story("delete deleted id")
@pytest.mark.delete_booking
def test_delete_deletedBooking(booking_client:BaseSession, deleted_id_for_delete_test):
    id = deleted_id_for_delete_test
    allure.dynamic.title(f"try to delete deleted id {id}")
    allure.dynamic.description(f"trying to delete deleted id {id} to check if the status code is 405 and a json message confirming that  deleting failed")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=405,id=id)
    with allure.step("validating response"):
        exe.delete_response_Test()
@allure.epic("get data")
@allure.feature("deleted id")
@pytest.mark.delete_booking
def test_get_deleted_booking(booking_client:BaseSession, deleted_id_for_get_test):
    id = deleted_id_for_get_test
    allure.dynamic.title(f"get deleted  id {id}")
    allure.dynamic.description(f"trying to get deleted id {id} to check if the status code is 404 and a json message confirming that failed getting the id")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=404,id=id)
    with allure.step("validating response"):
        exe.get_response_Test()