from utils.logger import logger as log
import allure,json
import requests
class BaseSession:
    def __init__(self, session:requests.Session, base_url:str):
        self.session = session
        self.base_url = base_url
        self.log=log()
    def end_point(self, route :str):
        """Set the API endpoint URL by appending route to base_url."""
        self.log.info(f"_________API endpoint pointed to {route}_________")
        self.url=self.base_url+route
    def generate_token(self, data:dict):
        self.log.info(f"getting token with data : {data}")
        allure.attach(body=json.dumps(data,indent=4),name="data",attachment_type=allure.attachment_type.JSON)
        result=self.session.post(self.url, json=data)
        try:
            self.log.info(f"generated token : {result.json()["token"]} for status code : {result.status_code}")
        except (ValueError,KeyError,requests.RequestException) as e:
            self.log.info(f"token generation failed : {str(e)}")
        return result
    def set_token(self, token:str):
        self.session.headers.update({'Cookie': f'token={token}'})
    def create_booking(self, data:dict, headers:dict|None=None):
        return self.session.post(self.url, json=data, headers=headers)
    def get_booking(self,id:int|None=None,headers:dict|None=None):
        if id:
            url=self.url+f"/{id}"
        else:
            url=self.url
        return self.session.get(url, headers=headers)
    def update_booking(self, id:int, data:dict, headers:dict|None=None):
        url=self.url+f"/{id}"
        self.log.debug(f"Headers: {headers}")
        return self.session.put(url, json=data, headers=headers)
    def delete_booking(self, id:int):
        url=self.url+f"/{id}"
        return self.session.delete(url)
    def partial_update_booking(self, id:int, data:dict, headers:dict|None=None):
        url=self.url+f"/{id}"
        return self.session.patch(url, json=data, headers=headers)
    def get_token(self):
        try:
            return self.session.headers["Cookie"]
        except KeyError:
            self.log.warning("Token not found in headers")
            return None