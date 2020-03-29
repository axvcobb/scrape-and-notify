from twilio.rest import Client


class Twilio:

    def __init__(self, sid, auth):
        self.client = Client(sid, auth)

    def send_text(self, body, from_number, to_number):
        self.client.messages.create(
            body=body,
            from_=from_number,
            to=to_number
        )
