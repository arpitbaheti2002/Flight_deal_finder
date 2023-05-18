from twilio.rest import Client
import smtplib

class NotificationManager():
    def __init__(self):
        self.ACCOUNT_SID = "ACfbb46efc5cfd12eb6907ef21f6a2327d"
        self.AUTH_TOKEN = "bce6ae5ac3aa835075543897d851d1cd"
        self.PHONE_NO = "+14706466811"
        self.email = "arpitbaheti3006@gmail.com"
        self.password = "iutylssteurjaqdv"

    def send_sms(self, notification):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages.create(
            to='+918972972319',
            from_=self.PHONE_NO,
            body=notification
        )   
        print(message.status)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)

            for email in emails:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg = f"Subject:Low Flight Deal!\n\n{message}"
                )
