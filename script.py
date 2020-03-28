from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
import config


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


a = scrape(config.scrape_url, config.scrape_text)


if a:
    notify()
