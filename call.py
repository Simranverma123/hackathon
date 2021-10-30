from twilio.rest import Client
import speak
def call() :
    client = Client("",
                "")
    call= client.calls.create(twiml='<Response><Say>Please Come Help me</Say></Response>',to = "+918210410103",  from_ = "+13512072081" )
    print("done")  
    speak.speak("Successfully Called to Doctor Sir!")  

