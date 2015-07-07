from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACc573799cf4313e6a9647663a24889965"
auth_token  = "abaab91965283bdab1e3e705e3f73289"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="test",
    to="+447539242202",    # Replace with your phone number
    from_="+441224518347") # Replace with your Twilio number
print message.sid
