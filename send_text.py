
from twilio.rest import TwilioRestClient

account_sid = "AC6aee6dd992c8c8b6f72741fe0df77e3c" # Your Account SID from www.twilio.com/console
auth_token  = "4ac7ff28ea4a3c8078ec03b559aa68e6"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+919990487763", 
    from_="+16193770849",
    body="hello")

print(message.sid)
