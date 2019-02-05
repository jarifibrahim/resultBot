import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate, formataddr
from config import USERNAME, PASSWORD, EMAIL_SMTP, SEND_TO, CC, BCC


def send_mail(subject, text, send_to=SEND_TO, cc=CC, bcc=BCC, files=None):

    msg = MIMEMultipart()
    msg['From'] = formataddr(("ResultBot", USERNAME))
    msg['To'] = COMMASPACE.join(send_to) if type(send_to) is list else send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    if cc:
        msg['Cc'] = COMMASPACE.join(cc) if type(cc) is list else cc
        send_to += [msg['Cc']]
    if bcc:
        bcc = COMMASPACE.join(bcc) if type(bcc) is list else bcc
        send_to += [bcc]

    msg.attach(MIMEText(text))
    # Attach files to email
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            attachment = 'attachment; filename="%s"' % basename(f)
            part['Content-Disposition'] = attachment
            msg.attach(part)

    smtp = smtplib.SMTP(EMAIL_SMTP)     # smtp initialization 1
    smtp.ehlo()                         # smtp initialization 2
    smtp.starttls()                     # smtp initialization 3
    send(smtp, send_to, msg)


def send(smtp, send_to, msg):
    try:
        smtp.login(USERNAME, PASSWORD)
        smtp.sendmail(USERNAME, send_to, msg.as_string())
        print '\033[92m' + 'Successfully sent the mail' + '\033[0m'
    except smtplib.SMTPAuthenticationError:
        err = ('\033[91m' + 'ERROR: Unable to send email. '
               'Username or Password incorrect.'
               ' Please verify username/password and try again.'
               '\033[0m')
        print err
    except Exception as e:
        print '\033[91m' + 'ERROR: Something went wrong. Email not sent.'
        print e
        print '\033[0m'
    finally:
        smtp.close()
