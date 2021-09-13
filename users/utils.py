from django.core.mail import send_mail


def send_verification_code(user, verification_code):
    send_mail('Verification code', verification_code, 'yara company', [user], fail_silently=False)
