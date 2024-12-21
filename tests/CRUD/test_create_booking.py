from http.client import responses
from os import utime

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helper.payload_manager import *
from src.helper.common_verification import *
from src.helper.api_requests_wrapper import post_request
from src.utilis.utilis import util

class TestCreateBooking(object):

    def test_create_booking(self):

        response=post_request(url=APIConstants.url_create_booking(),
                               headers=util().common_header_json(),
                               auth=None,payload=payload_create_booking(),in_json=False)

        booking_id= response.json()["bookingid"]

        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(booking_id)

