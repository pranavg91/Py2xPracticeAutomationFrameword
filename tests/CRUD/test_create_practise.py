from http.client import responses
import pytest
import allure
from src.constants.api_constants import *
from src.helper.payload_manager import *
from src.helper.common_verification import *
from src.helper.api_requests_wrapper import *
from src.utilis.utilis import *


class Test_create_booking2(object):

    def test_create_booking(self):
        response = post_request(url=APIConstants().url_create_booking(),
                                auth=None, in_json=False,
                                payload=payload_create_booking(),
                                headers=util().common_header_json())
        print(response.json())
        print("status code :", response.status_code)