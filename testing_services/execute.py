from testing_services.validate import Test_response
from utils.api_client import BaseSession
class Execute_with_data:
    def __init__(self,fed_session:BaseSession,data:dict|None=None,code:int|None=None,id:int|None=None)->None:
        self.fed_session=fed_session
        self.code=code
        self.data=data
        self.id=id
        self.response=None
    def auth_post_test(self,headers:dict)->None:
        print(headers,type(headers)," is the headers")
        print(self.fed_session.url," is the url ",self.fed_session.get_token()," is the token")
        self.response=self.fed_session.create_booking(self.data,headers=headers)
        Test_response(self)
    def auth_edit_test(self,headers:dict)->None:
        print(headers,type(headers)," is the headers")
        print(self.fed_session.url," is the url ",self.fed_session.get_token()," is the token")
        self.response=self.fed_session.update_booking(self.id,self.data,headers=headers)
        Test_response(self)
    def post_response_Test(self)->None:
        self.response=self.fed_session.create_booking(self.data)
        Test_response(self,Post_method=True)
    def get_response_Test(self)->None:
        self.response=self.fed_session.get_booking(self.id)
        Test_response(self)
    def update_response_Test(self)->None:
        print(self.id,"is the id to be updated")
        self.response=self.fed_session.update_booking(self.id,self.data)
        print(self.response.status_code,"is the status code of update response")
        try: print(self.response.json(),"is the json response of update response")
        except Exception as e: print(f"Response is not in JSON format. Error: {e}")
        Test_response(self)
    def partial_update_response_Test(self)->None:
        data=self.fed_session.get_booking(self.id).json()
        expected_data={**data,**self.data}
        self.response=self.fed_session.partial_update_booking(self.id,self.data)
        self.data=expected_data
        Test_response(self)
    def delete_response_Test(self)->None:
        print(self.id," is the id going to be deleted")
        self.response=self.fed_session.delete_booking(self.id)
        print(self.response.status_code, " is the deleted id deleted response")
        Test_response(self)