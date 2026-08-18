import requests
s=requests.Session()
base_url = 'https://restful-booker.herokuapp.com'
s.headers.update({'Content-Type': 'application/json',
                'Accept': 'application/json'})
auth_payload = {
    "username": "admin",
    "password": "password123"
}
token = s.post(
    f"{base_url}/auth",
    json={
        "username": "admin",
        "password": "password123"
    }
).json()["token"]
print(token)
s.headers.update({"Cookie": f"token={token}"})
payload={"firstname":"updated_name","lastname":"updated_lastname","totalprice":123,"depositpaid":True,"bookingdates":{"checkin":"2024-01-01","checkout":"2024-01-10"},"additionalneeds":"updated_needs"}
postr=s.post(f"{base_url}/booking", json=payload)
id=postr.json().get("bookingid")
dr=s.delete(f"{base_url}/booking/{id}")
print(dr.status_code)
try:
    print(dr.json())
    print(dr.content)
    print(dr.text)
except:pass
ddr=s.delete(f"{base_url}/booking/{id}")
print(ddr.status_code)
try:print(ddr.json())
except:pass
