class util(object):


    def common_header_json(self):
        headers = {"Content-Type": "application/json"}

        return headers


    def common_header_put_patch_basic_auth(self):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Basic YWRtaW46cGzc3dvcmQxMjM="
                   }

        return headers


    def common_header_put_token(self,token):
        headers = {"Content-Type": "application/json",
                   "Cookie": "token=" + str(token)
                   }

        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

