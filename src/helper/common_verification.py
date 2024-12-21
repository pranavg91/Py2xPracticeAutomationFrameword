def verify_http_status_code(response_data,expect_data):
    assert response_data.status_code == expect_data,"expected HTTP status code"



def verify_json_key_for_not_null(key):
    assert key !=0,"Key is not empty" + key
    assert key >0,"Failed-Key is greater than 0"

def verify_delete_response(response):
    assert "Created" in response.text

