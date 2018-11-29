
# This file is responsible for sending sms using 3rd party APIs in lib.py, checking SMS status, 
# handling SMS errors.

from django.db.models.signals import post_save
from django.dispatch import receiver

from globals import SMS_STATUS_APPROVED, SMS_STATUS_CANCELLED, SMS_STATUS_INVALID_SMS
from .models import SmsLog
from .lib import send_1s2u_sms


@receiver(post_save, sender=SmsLog)
def send_sms(sender, instance, created, **kwargs):

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


def check_internal_status(pk):
    # returns the status of the sms with the given pk, does not do an external check with 3rd party.
    # param: pk = Primary key in SmsLog Model.

    try:
        message = SmsLog.objects.get(pk=pk)
        return message.status
    except SmsLog.DoesNotExist:
        return SMS_STATUS_INVALID_SMS
