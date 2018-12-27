
# This file is responsible for sending sms using 3rd party APIs in lib.py, checking SMS status, 
# handling SMS errors.

from django.db.models.signals import post_save
from django.dispatch import receiver

from globals import SMS_STATUS_APPROVED
from .models import SmsLog
from .lib import send_1s2u_sms


@receiver(post_save, sender=SmsLog)
def send_sms(sender, instance, created, **kwargs):
    res = {}

    if created:
        res = send_1s2u_sms(number=instance.number, message=instance.message, sender=instance.sender)
        if res['error']:  # if an error occured.
            instance.response = res['error']
        else:
            instance.message_id = res['message_id']
            instance.status = SMS_STATUS_APPROVED
            instance.save()

