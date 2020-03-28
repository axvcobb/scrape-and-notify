from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
import config

print("Script is running")


def scrape(url, text):
    page = requests.get(url).content
    soup = BeautifulSoup(page, "html.parser")

    return soup.find_all(string=text)


def notify():
    account_sid = config.twilio_sid
    auth_token = config.twilio_auth
    client = Client(account_sid, auth_token)

    client.messages \
        .create(
            body=config.twilio_body,
            from_=config.twilio_from,
            to=config.twilio_to
        )


# If scrape doesn't find the text, it returns an empty array.
# If it finds something, it triggers the notify() function
if scrape(config.scrape_url, config.scrape_text):
    notify()
