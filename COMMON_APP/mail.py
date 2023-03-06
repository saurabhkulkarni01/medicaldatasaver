import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
API_KEY="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"

def welcomemail():
    message = Mail(
        from_email='gulshantelkar16@gmail.com',
        to_emails='saurabhmk01@gmail.com',
        subject='Welcome to healthcare record system app!',
        html_content='<strong>Welcome to Medical History Saver ! We hope we will provide you all the necessary functionalities and better user experience !</strong>')
    # try:
    sg = SendGridAPIClient(API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    # except Exception as e:
    #     print(e.message)