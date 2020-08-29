# with shell

from twilio.rest import TwilioRestClient
accountSID = 'xxxxxxx'
authToken = 'xxxxxxx'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+134456'
myCellPhone = '+432758'
message = twilioCli.message.create(body='Mr. Watson - come here.', \
                                    from_=myTwilioNumber,to_=myCellPhone)
