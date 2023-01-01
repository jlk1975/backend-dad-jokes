from twilio.rest import Client

def send(account_sid, auth_token, joke, contact_record, twilio_from_number):
    recipient = contact_record['name']
    recipient_number = contact_record['number']
    print("Sending joke to " + recipient + " @ " + recipient_number + "..." + "From Twilio Number " + twilio_from_number)
    print(joke)
    client = Client(account_sid, auth_token)
    message = client.messages \
                     .create(
                          body=joke,
                          from_=twilio_from_number,
                          to=recipient_number
                      )
    return(message.sid)