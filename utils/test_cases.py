from utils.routes import Routes
from utils.logger import logger as log
import time
import requests
from utils.data_loader import data_loader

class TestCases:
    """Generates and manages test data for API testing scenarios."""
    booking_url=Routes.base_url+Routes.booking
    loging_url=Routes.base_url+Routes.login
    session=requests.session()
    @classmethod
    def booking(cls):
        return data_loader("test_data/booking/valid_data.json")
    @classmethod
    def booked_data(cls):
        load=data_loader("test_data/booking/booked_data.json")
        cls.session.post(cls.booking_url,json=load)
        time.sleep(1)
        return load
    @classmethod
    def invalid_booking(cls):
        return data_loader("test_data/booking/invalid_data.json")
    @classmethod
    def get(cls):
        load=data_loader("test_data/get_data.json")
        log().debug(f"Loaded test data: {load}")
        Ids=[]
        data=[]
        for i in load:
            response=cls.session.post(cls.booking_url,json=i).json()
            id=response["bookingid"]
            D=response["booking"]
            Ids.append(id)
            data.append(D)
            time.sleep(1)
        return zip(Ids,data)
    @classmethod
    def delete(cls):
        load=data_loader("test_data/delete/data.json")
        Ids=[]
        for _ in load:
            response=cls.session.post(cls.booking_url,json=_).json()
            id=response["bookingid"]
            Ids.append(id)
            time.sleep(1)
        return Ids
    @classmethod
    def deleted0(cls):
        load=data_loader("test_data/delete/deleted0_data.json")
        log().debug(f"Test data loaded: {load}")
        response=cls.session.post(cls.booking_url,json=load).json()
        id=response["bookingid"]
        log().debug(f"Post response ID: {id}")
        r=cls.session.delete(cls.booking_url+"/"+str(id))
        log().debug(f"Delete response status: {r.status_code}")
        time.sleep(1)
        return id
    @classmethod
    def deleted1(cls):
        load=data_loader("test_data/delete/deleted1_data.json")
        log().debug(f"Test data loaded: {load}")
        response=cls.session.post(cls.booking_url,json=load).json()
        id=response["bookingid"]
        log().debug(f"Post response ID: {id}")
        r=cls.session.delete(cls.booking_url+"/"+str(id))
        log().debug(f"Delete response status: {r.status_code}")
        time.sleep(1)
        return id
    @classmethod
    def update(cls):
        load=data_loader("test_data/edit/update_ids.json")
        id=cls.session.post(cls.booking_url,json=load).json()["bookingid"]
        return id
    @classmethod
    def partial_update(cls):
        load=data_loader("test_data/edit/partial_update_ids.json")
        id=cls.session.post(cls.booking_url,json=load).json()["bookingid"]
        return id
    @classmethod
    def auth_put(cls):
        load=data_loader("test_data/auth/put_token.json")
        TestCases=[]
        for L in load:
            id=cls.session.post(cls.booking_url,json=L["data"]).json()["bookingid"]
            if L["header"]=="":
                L["header"]=None
            TestCases.append({"id":id,"expected_code":L["expected_code"],"header":L["header"]})
        return TestCases
    @classmethod
    def auth_post(cls):
        load=data_loader("test_data/auth/post_token.json")
        TestCases=[]
        for L in load:
            if L["header"]=="":
                L["header"]=None
            L["expected_code"]=int(L["expected_code"])
            TestCases.append(L)
        return TestCases
    @classmethod
    def login(cls):
        load=data_loader("test_data/login/data.json")
        return load
    @classmethod
    def invalid_login(cls):
        load=data_loader("test_data/login/invalid_data.json")
        return load
    @classmethod
    def put_data(cls):
        load=data_loader("test_data/edit/put_data.json")
        return load