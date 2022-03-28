from cgitb import text
from email import message
from multiprocessing.connection import Listener
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info.lower())
            return info.lower()
    except:
        pass

def send_mail(receiver,subject,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('learninganesh@gmail.com','Learninganesh@18')
    email = EmailMessage()
    email['From'] = 'learninganesh@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    

email_dict = {
    'ganesh' : 'gk9801421579@gmail.com',
    'mukesh' : 'mk7462955309@gmail.com',
    'kishan': '5822kr@gmail.com',
    'love':  'srivastavluv007@gmail.com'
}

def get_email_info():
    talk('to whome you want to send email')
    name = get_info()
    receiver = email_dict[name]
    talk("waht is your subject to send in email")
    subject = get_info()
    talk('what is message for email.')
    message = get_info()
    send_mail(receiver,subject,message)

g= get_email_info()