import sys
import os

BASE_URL = 'http://exam.nmu.ac.in/online%20result/aspx/online%20result.aspx'

if len(sys.argv) != 2:
    msg = ("Usage: python main.py <Faculty>"
           "\n\nCheck " + BASE_URL +
           " for the list of faculties.")
    print (msg)
    exit(1)

FACULTY = sys.argv[1]
BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
DL_FOLDER = BASE_DIR + FACULTY + '-results/'
DL_FILE_NAME = DL_FOLDER + 'downloaded_files.txt'
PATH_TO_PHANTOMJS = BASE_DIR + 'phantomjs'

# email authentication credentials
USERNAME = 'jarifibrahim@gmail.com'
PASSWORD = ''  # App password
EMAIL_SMTP = 'smtp.gmail.com:587'

# sms authentication credentials
URL = 'http://www.way2sms.com/api/v1/sendCampaign'
APIKEY = '' # way2sms apiKey
SECRETKEY = '' # way2sms secretKey
PHONENO = # receiver's valid phone number(indian) without country code

# The following three variables should be set
SEND_TO = ['jarifibrahim@gmail.com']
CC = []
BCC = []
