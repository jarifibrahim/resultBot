import requests
import json
import general

URL = 'http://www.way2sms.com/api/v1/sendCampaign'


# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
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
        response = sendPostRequest(URL, apiKey, secretKey, 'stage', phoneNo, 'WAYSMS', message )
        # print response if you want
        print (response.text)
    except Exception as e:
        print(e)
    finally :
        print()
        exit()
