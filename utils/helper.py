##used to store values in a circular list
from utils.data_loader import data_loader
import time  
class Auth:
    def __init__(self):
        self.Token=None 
def get_token(response):
    try:
        json_response=response.json()
        return json_response.get('token')
    except:
        return None
def get_data(booking_client,data):
    id=[]
    body=[]
    for load in data_loader("Test_cases/sample_data.json"):
        response=booking_client.create_booking(load)
        json=response.json()
        id.append(json["bookingid"])
        body.append(json["booking"])
        time.sleep(2)
    return {"ids":id,"data":body}
def get_ids(booking_client,data):
    ids=get_data(booking_client,data)["ids"]
    return ids