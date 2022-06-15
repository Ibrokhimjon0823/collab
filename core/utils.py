from email.message import EmailMessage
import smtplib
import threading

########################################################
#########  User email related utils #############
########################################################
def send_email(to_email: str = None, message: str = None):
    SMTP_EMAIL = "ibrokhimjonmakhamadaliev@gmail.com"
    SMTP_PASSWORD = "Mr_coolman_99"

    from_email = SMTP_EMAIL
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = 'Customer Request'
    msg['From'] = from_email
    msg['To'] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(from_email, SMTP_PASSWORD)
    server.send_message(msg)
    server.close()


def send_registration_email(to_email: str = None, message: str = None):
    data = {
        'to_email': to_email,
        'message': message
    }
    t = threading.Thread(target=send_email, kwargs=data)
    t.setDaemon(True)
    t.start()


def request_create_email_message(email: str = None, password: str = None):
    message = f'Hello, \nWe received a request for account registration.\n' \
              f'Please use following credentials to enter the platform\n\n'
    return message