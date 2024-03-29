
# This file is responsible for sending sms using 3rd party APIs in lib.py, checking SMS status, 
# handling SMS errors.

from django.db.models.signals import post_save
from django.dispatch import receiver

from globals import SMS_STATUS_APPROVED, SMS_STATUS_CANCELLED, SMS_STATUS_INVALID_SMS
from .models import SmsLog
from .lib import send_1s2u_sms


@receiver(post_save, sender=SmsLog)
def send_sms(sender, instance, created, **kwargs):
    """
    :param instance: of SmsLog model
    Listen's to a post save signal on the model SmsLog and sends the sms to the sms provider only if the instance
    object is a new one (created)
    """
    if created:
        res = send_1s2u_sms(number=instance.number, message=instance.message, sender=instance.sender)

        if res['success']:  # if the sms was sent successfully, update the message_id and status
            instance.message_id = res['message_id']
            instance.status = SMS_STATUS_APPROVED
            instance.save()
        else:
            instance.response = res['error']  # if the sms was not sent, update the response and the status.
            instance.status = SMS_STATUS_CANCELLED
            instance.save()

