from src.helper.payload_manager import *
from src.constants.api_constants import *
from src.helper.api_requests_wrapper import *
from src.helper.common_verification import *
from src.constants.api_constants import *
import iniconfig
from tests.CRUD.test_CRUD import *


class Test_create_update(object):
    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(),
                                headers=util().common_header_json(),
                                payload=payload_to_create_token(),
                                auth=None, in_json=False)
        token = response.json()["token"]
        verify_http_status_code(response_data=response, expect_data=200)
        return token
    @pytest.fixture()
    def get_create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None, in_json=False,
                                headers=util().common_header_json(),
                                payload=payload_create_booking())

        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id


    def test_create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None, in_json=False,
                                payload=payload_create_booking(),
                                headers=util().common_header_json())
        bookingid=response.json()["bookingid"]
        print(response.json())
        verify_json_key_for_not_null(key=bookingid)

    def test_update_booking(self,get_create_booking,create_token):
        booking_id=get_create_booking
        token=create_token
        PUT_URL=APIConstants.url_put_patch(booking_id=booking_id)
        response=put_request(url=PUT_URL,headers=util().common_header_put_token(token=token),
                    auth=None,payload=payload_create_booking(),in_json=False)

        verify_http_status_code(response_data=response,expect_data=200)

    def test_get_booking(self,get_create_booking):
        booking_id=get_create_booking
        GET_URL=APIConstants.url_get_booking(booking_id=booking_id)

        response =get_request(url=GET_URL,auth=None)
        print(response.json())
        assert "Pranav" in response.json()["firstname"]
        verify_http_status_code(response_data=response,expect_data=200)







