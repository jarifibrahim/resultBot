import requests
from requests import exceptions
import json
import general
from config import WAY2SMS_URL, SMS_API_KEY, SMS_SECRET_KEY, PHONE_NO


# send post request
def sendPostRequest(req_url, api_key, secret_key, use_type, phone_no, sender_id, text_message):
  req_params = {
  'apikey':api_key,
  'secret':secret_key,
  'usetype':use_type,
  'phone': phone_no,
  'message':text_message,
  'sender_id':sender_id
  }
  return requests.post(req_url, req_params)


def send_sms(message):
    try:
        # get response
        response = sendPostRequest(WAY2SMS_URL, SMS_API_KEY, SMS_SECRET_KEY, 'prod', PHONE_NO, 'WAYSMS', message )
        # print response if you want
        res =  response.text
        if 'success' in res:
            print('\033[92m' + 'Successfully sent the sms' + '\033[0m')
    except requests.exceptions.HTTPError as eh:
        print('\033[91m' + 'An HTTP error occurred. %s' %eh)
        print('\033[0m') 
    except requests.exceptions.ConnectionError as ec:
        print('\033[91m' + 'A Connection error occurred %s' %ec)
        print('\033[0m')
    except requests.exceptions.Timeout as et:
        print('\033[91m' + 'It is ConnectTimeout or ReadTimeout %s' %et)
        print('\033[0m')
    except Exception as e:
        print('\033[91m' + "Something went wrong. Failed to send SMS: %s" % e)
        print('\033[0m')
    finally :
         pass
