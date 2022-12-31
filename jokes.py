#!/usr/bin/python
import os
import json
import requests
import sms
from twilio.rest import Client

# Twilio setup
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Set the HTTP headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Set the API endpoint URL
url = "https://icanhazdadjoke.com"

# Send the request to the API endpoint
# response = requests.get(url, headers=headers)
# data = response.json()
# joke = data['joke']

# Next, create a JSON file that contains all the phone numbers you want to send jokes to.
# Load that file into a python object using code like this
# with open('numbers.json') as f:
    # data = json.load(f)

# for number in data['numbers']:
    # print(number)
    # then turn the twilio code below into a function
    # and just call that function with each pass of this loop
    # to send an SMS to each phone number.
    # But , before you check this into github, variablize
    # the from phone number below, that way you don't have to check in
    # an actual phone number to github.

sms.send()