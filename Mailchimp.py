import json
import requests


class Mailchimp:

    def __init__(self, api_key):
        self.headers = \
            {
                "Host": "us19.api.mailchimp.com",
                "Authorization": "Basic " + api_key,
                "Content-Type": "application/json; charset=utf-8"
            }

    def trigger_email(self, url, email_address):
        data = \
            {
                'email_address': email_address,
                'merge_fields': {}
            }

        requests.post(url, headers=self.headers, data=json.dumps(data))
