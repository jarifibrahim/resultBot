import requests
import json
import general
from config import URL, APIKEY, SECRETKEY, PHONENO

# get request 
def send_post_request(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


def send_sms(message):
    try:
        # get response
        response = send_post_request(URL, APIKEY, SECRETKEY, 'stage', PHONENO, 'WAYSMS', message )
        # print response if you want
        print (response.text)
    except Exception as e:
        print(e)
    finally :
        print()
        exit()
