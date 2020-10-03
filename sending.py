import smtplib
import getpass
import win32api
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
def login_email(email, password):
    status = ""
    try:
        smtp_object.login(email, password)
        status = True
    except smtplib.SMTPAuthenticationError:
        status = False
        pass
    return status
def email_input(email,password):
    try:
        if login_email(email, password):
            win32api.MessageBox(0, 'Login success', 'Status')
            return True
        else:
            win32api.MessageBox(0, 'Password incorrect', 'Status')
            return False
    except TypeError:
        win32api.MessageBox(0, 'Something went wrong', 'Status' )
        return False
def send_main():
    from_address =  'contract.pantakan'
    to_address = 'dward.the.2nd@gmail.com'
    subject = 'This is Test'
    message = 'Hello Website'
    msg = "Subject: "+subject+'\n'+message
    smtp_object.sendmail(from_address, to_address, msg)

if __name__ == "__main__":
    main()
