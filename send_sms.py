import requests
import json
import general

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

message = ''

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


def send_sms():
    # get response
    # response = sendPostRequest(URL, 'LMK6QOHJICCB90L41YCEXT0TFM1ZLZFE', '9MBTZATQ9I6ZDMFW', 'stage', '8329534793', 'WAYSMS', message )
    # print response if you want
    # print (response.text)
