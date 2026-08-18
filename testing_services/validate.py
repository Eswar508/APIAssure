from utils.assertions import Validate
def Test_response(values,Post_method=False):
    assert_True=Validate(values.response)
    print(values.response.status_code," is the status_code and ",values.code," is the expected status code")
    assert_True.assert_status_code(values.code) if values.code is not None else None
    if values.data and values.code ==200:
        assert_True.assert_booking_data_matches(values.data)
        assert_True.assert_id_is_int() if Post_method else None