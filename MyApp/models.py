from django.core.mail import send_mail
from django.db import models
class Dht(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 40:
            #envoyer un message sur telegrame
            import telepot
            token = '5974174053:AAERLTPbM-DfSUQFT2YbX3BYwcDILyI5E-k'
            rece_id = 1825312550
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, 'attention ! la temperature severe ')
            #envoyer un message sur email
            send_mail(
                'température dépasse la normale,',
                'anomalie dans la machine',
                'oumaima.elhamdami@ump.ac.ma',
                ['adnane.elkhatib@ump.ac.ma'],
                fail_silently=False)

            from twilio.rest import Client
            account_sid = 'AC10ed6a83bfa23043429f889b4bc0aa8f'
            auth_token = '7276ed8546bf457d6db26bc28ce9f158'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'attention ! temperature severe',
                from_='+19297326785',
                to='+212637392064',
            )
            print(message.sid)

        return super().save(*args, **kwargs)



