# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf99d181bee7652734862dd42cb0c7601'
auth_token = 'b13582320472c60b71fc7912e7c03ec2'
client = Client(account_sid, auth_token)

local = client.available_phone_numbers('US').local.list(
    in_region='NY',
    limit=20
)

for record in local:
    print(record.friendly_name)
