from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def SendWelcomeMessage(name,phone):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    body = "Wecome "+name+"to the Medical History Saver App"
    PhoneNumber="+91"+str(phone)
    message = client.messages \
                    .create(
                        body=body,
                        from_='+13396751065',
                        to='+919399296095'
                    )

    print(message.sid,"sms send")

def profileupdate(name,phone):
    account_sid = "ACe3bbdea044b7fb469c602d55ef4eec6a"
    auth_token = "eec86548586ab78b5461811be1188d38"
    client = Client(account_sid, auth_token)
    body = name+" Your Profile is updated on Medical History Saver App"
    PhoneNumber="+91"+str(phone)
    message = client.messages \
                    .create(
                        body=body,
                        from_='+13396751065',
                        to='+919399296095'
                    )

    print(message.sid,"sms send")

def appointmentcancellation(name,phone,date,reason,withname):
    account_sid = "ACe3bbdea044b7fb469c602d55ef4eec6a"
    auth_token = "eec86548586ab78b5461811be1188d38"
    client = Client(account_sid, auth_token)
    body = name+" your appointment on"+date+" with"+withname+" is cancelled due to reason:"+ reason + " follow Medical History Saver App for furthur updates"
    PhoneNumber="+91"+str(phone)
    message = client.messages \
                    .create(
                        body=body,
                        from_='+13396751065',
                        to='+919399296095'
                    )

    print(message.sid,"sms send")

def appointmentbooked(name,phone,date,withname):
    account_sid = "ACe3bbdea044b7fb469c602d55ef4eec6a"
    auth_token = "eec86548586ab78b5461811be1188d38"
    client = Client(account_sid, auth_token)
    body = name+" your appointment is booked on"+date+" with"+withname +" follow Medical History Saver App for furthur updates"
    PhoneNumber="+91"+str(phone)
    message = client.messages \
                    .create(
                        body=body,
                        from_='+13396751065',
                        to='+919399296095'
                    )

    print(message.sid,"sms send")

def sendsms():
    account_sid = "ACe3bbdea044b7fb469c602d55ef4eec6a"
    auth_token = "eec86548586ab78b5461811be1188d38"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Welcome to Medical History Saver App",
                        from_='+13396751065',
                        to='+919399296095'
                    )

    print(message.sid,"sms send")
