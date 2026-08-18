from utils.logger import logger as log

class Validate:
    """Validates API response data, status codes, and response structure."""
    
    def __init__(self,response):
        self.response=response
        self.logger=log()
        try: self.json=response.json()
        except ValueError: self.json={}
        self.status_code=response.status_code
    def assert_token_is_string(self):
        #first check if 'token' is present in the response json, then check if it's a string
        assert self.json
        assert 'token' in self.json
        assert isinstance(self.json.get('token'), str)
    def assert_status_code(self, expected_code):
        assert self.status_code == expected_code    
    def assert_token_not_present(self):
        assert 'token' not in self.json
    def assert_id_is_int(self):
        assert 'bookingid' in self.json
        assert isinstance(self.json.get('bookingid'), int)
    def assert_booking_data_matches(self, expected_data):
        if "booking" not in self.json:
            response_data=self.json
            self.logger.debug(f"Response data: {response_data}")
            self.logger.debug(f"Expected data: {expected_data}")
            assert response_data==expected_data
        else:
            response_data=self.json.get('booking')
            assert response_data==expected_data