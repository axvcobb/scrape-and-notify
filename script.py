from bs4 import BeautifulSoup
from Twilio import Twilio
from Mailchimp import Mailchimp
import requests
import config


# Searches the given 'url' page for the 'text'
# Returns an empty array if the 'text' isn't found
# If the 'text' is found, it returns an array with
#   that many occurrences
def scrape(url, text):
    page = requests.get(url).content
    soup = BeautifulSoup(page, "html.parser")

    return soup.find_all(string=text)


# Fires off a Twilio text and triggers a Mailchimp email
def notify():
    Twilio(config.twilio_sid, config.twilio_auth).\
        send_text(config.twilio_body, config.twilio_from, config.twilio_to)
    Mailchimp(config.mailchimp_key).\
        trigger_email(config.mailchimp_url, config.mailchimp_email)


# If scrape doesn't find the text, it returns an empty array.
# If it finds something, it triggers the notify() function
if scrape(config.scrape_url, config.scrape_text):
    notify()
