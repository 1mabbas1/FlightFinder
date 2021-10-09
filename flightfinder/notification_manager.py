from twilio.rest import Client

#Enter your own twilio details and phone number.
TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_VIRTUAL_NUMBER = '+123456'
TWILIO_VERIFIED_NUMBER = '+123456'

#Sends a text message with flight details.
class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
