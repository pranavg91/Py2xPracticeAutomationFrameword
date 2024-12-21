class APIConstants(object):

    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com/"


    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_get_booking(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def url_put_patch(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
