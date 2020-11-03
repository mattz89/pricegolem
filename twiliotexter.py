# Standard Library Imports
import os

# Third Party Imports
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


# Twilio Config
twilio_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_number = os.environ.get('TWILIO_NUMBER')
client = Client(twilio_sid, twilio_token)


# Twilio Sending Text
def send_text(url, selling_price, phone):
    valid_check = is_valid_number(phone)
    message = f"Price changed to { selling_price }! Buy now: \n { url }"
    if valid_check == True:
        client.messages.create(to=phone, from_=twilio_number, body=message)
        print("Text sent successfully")
    else:
        print("Failed to send.")


# Twilio Validating Number to Text
def is_valid_number(number):
    try:
        client.lookups.phone_numbers(number).fetch(type="carrier")
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e