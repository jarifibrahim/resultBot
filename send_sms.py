import requests
from requests import exceptions
import json
import general
from config import WAY2SMS_URL, SMS_API_KEY, SMS_SECRET_KEY, PHONE_NO

def send_sms(message):
    try:
        req_params = {
        'apikey':SMS_API_KEY,
        'secret':SMS_SECRET_KEY,
        'usetype':'prod',
        'phone': PHONE_NO,
        'message':text_message,
        'sender_id':'WAYSMS'
        }
        response = request.post(WAY2SMS_URL, req_params)

        res =  response.text
        if 'success' in res:
            print('\033[92m' + 'Successfully sent the sms' + '\033[0m')
    except Exception as e:
        print('\033[91m' + "Failed to send SMS: %s" % e)
        print('\033[0m')
