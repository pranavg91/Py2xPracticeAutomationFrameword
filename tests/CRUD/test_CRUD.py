from http.client import responses
from os.path import isabs

import allure
import pytest
import allure
from src.constants.api_constants import *
from src.helper.api_requests_wrapper import *
from src.helper.common_verification import *
from src.helper.payload_manager import *
from src.utilis.utilis import *

@allure.title("Testing CRUD operation")
@allure.description("Testing end to end CRUD operation")
class TestCRUD(object):
    @pytest.fixture()
    def create_token(self):
        response=post_request(url=APIConstants.url_create_token(),
                              headers=util().common_header_json(),
                              payload=payload_to_create_token(),
                              auth=None,in_json=False)
        token=response.json()["token"]
        verify_http_status_code(response_data=response,expect_data=200)
        return token


    @pytest.fixture()
    def get_create_booking(self):
        response =post_request(url=APIConstants.url_create_booking(),
                               auth=None,in_json=False,
                               headers=util().common_header_json(),
                               payload=payload_create_booking())

        booking_id=response.json()["bookingid"]
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    def test_update_booking(self,get_create_booking,create_token):
        booking_id = get_create_booking
        token=create_token
        put_url =APIConstants.url_put_patch(booking_id=booking_id)

        response=put_request(url=put_url,headers=util().common_header_put_token(token=token),
                             auth=None,in_json=False,payload=payload_create_booking())
        print(response.json())


    def test_delete_booking(self,get_create_booking,create_token):

        booking_id=get_create_booking
        token = create_token

        delete_url=APIConstants.url_put_patch(booking_id=booking_id)

        response= delete_requests(url=delete_url,auth=None,
                                  in_json=False,
                                  headers=util().common_header_put_delete_patch_cookie(token=token))
        verify_http_status_code(response_data=response,expect_data=201)
        verify_delete_response(response=response)
        print("\nDelete api response is",response.text)







