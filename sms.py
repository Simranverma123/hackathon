from twilio.rest import Client
import speak

def sms(text) :
    client = Client("" , "")
    client.messages.create(to = ["+918210410103"],
       from_ = "+13512072081",
       body = text)
    print("done!")
    speak.speak("Sent SMS Successfully Sir !")
