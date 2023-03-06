from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
account_sid = 'ACe3bbdea044b7fb469c602d55ef4eec6a'
auth_token = 'eec86548586ab78b5461811be1188d38'
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    message = request.POST["Body"]
    sender_name = request.POST["ProfileName"]
    sender_number = request.POST["From"]
    if message=="hi":
        client.messages.create(
            from_='whatsapp:+14155238886',
            body='How can we help you ?',
            to='whatsapp:+919399296095'
            )
    


def welcomemsg():
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Welcome to Medical History Saver ! We hope we will provide you all the necessary functionalities and better user experience !',
    to='whatsapp:+919399296095'
    )
    print(message.sid)

