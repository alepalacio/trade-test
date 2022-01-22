from django.core.mail import send_mail, EmailMessage

class EmailUtil:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['subject'], body=data['body'], to=[data['to_email']])
        email.fail_silently=False
        email.send()