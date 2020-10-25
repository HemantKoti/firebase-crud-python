# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf99d181bee7652734862dd42cb0c7601'
auth_token = 'b13582320472c60b71fc7912e7c03ec2'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello World from Unilend.",
                    from_='+18454437370',
                    to='+17169397014'
                )

print(message.sid)
