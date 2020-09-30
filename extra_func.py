import smtplib
import pyqrcode
from googletrans import Translator
import requests
import phonenumbers
from phonenumbers import carrier
from yahoo_fin import stock_info as si
import pyjokes
import random



def set_reminder(set_date,set_time,task):

    data = str(set_time)+' '+str(set_date)+' '+ str(task)

    with open('to-do-list', 'a') as f:
        f.write(data)

    speak('reminder is set now!')

# smtplib

def sendEmail(to, content):
    ''' send email '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


# pyqrcode

def qenerate_qr_code_of(link):
	''' generate QR code of link '''
	url = pyqrcode.create(link_)
	url.svg("Qrcode.svg", scale=10)

# Translator 

def translate(data,language):

    Translator = Translator()
    Translated = Translator.translate(data,dest=language)

    return Translated.text

# Instagram                     requests
def Instagram_followers_of(username):

    url = 'https://www.instagram.com/'+username
    result = requests.get(url).text

    start = '"edge_followed_by":{"count":'
    end = '},"followed_by_viewer"'
    result = str(result[result.find(start)+len(start):result.rfind(end)])

    return result

# phonenumbers
  
def get_service_provider_of(phonenumber):

    service_provider = phonenumbers.parse(phonenumber)

    return carrier.name_for_number(service_provider,"en")


def stock_price_of(company):

    price = "$ "+si.get_live_price(company)

    return price



def  jokes():

    number = random.randint(0, 96)
    joke = pyjokes.get_jokes()

    return joke[number]
