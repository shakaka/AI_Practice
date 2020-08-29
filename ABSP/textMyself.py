# define the textmyself function

accountSID = 'xxxxxxxxx'
authToken ='xxxxxxxxxxx'
myNumber = '+123445'
twilioNumber = '+424625'

from twilio.rest import TwilioRestClient:

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.message.create(body=message, from_=twilioNumber, to_=myNumber)
    
