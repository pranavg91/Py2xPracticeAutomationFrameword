import json
import requests

def get_request(url,auth):
    get_response=requests.get(url=url,auth=auth)
    return get_response

def post_request(url,auth,headers,payload,in_json):
    post_responses =requests.post(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return post_responses.json()
    return post_responses


def put_request(url,headers,payload,in_json,auth):
    put_response=requests.put(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response

def delete_requests(url, headers, auth, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
