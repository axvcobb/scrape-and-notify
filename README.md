# scrape-and-notify

## Overview
Just a simple Python script that scrapes a given webpage and searches for a specified string. If the string is found on said webpage, it fires off a Twilio text and triggers a Mailchimp email.

## Example config.py
```
twilio_sid = ""
twilio_auth = ""
twilio_body = ""
twilio_from = ""
twilio_to = ""

scrape_url = ""
scrape_text = ""

mailchimp_key = ""
mailchimp_url = ""
mailchimp_email = ""
```
