from faker import Faker

def payload_create_booking():
    payload={
            "firstname": "Pranav",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_dyamic_booking():
    fake = Faker()
    payload={

            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": fake.random_int(100,1000),
            "depositpaid": fake.boolean(),
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": fake.random_element(elements="Breakfast")
    }
    return payload


def payload_to_create_token():
    payload = {
    "username" : "admin",
    "password" : "password123"
}
    return payload