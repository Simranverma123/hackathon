from twilio.rest import Client
import speak
def call() :
    client = Client("ACc7d414df5a2772ddffae6e54f79f6756",
                "39c30d224f05a2758f49480aa13305e3")
    call= client.calls.create(twiml='<Response><Say>Please Come Help me</Say></Response>',to = "+918210410103",  from_ = "+13512072081" )
    print("done")  
    speak.speak("Successfully Called to Doctor Sir!")  

