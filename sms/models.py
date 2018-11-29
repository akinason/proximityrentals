from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from globals import SMS_STATUS_SUBMITTED, DEFAULT_SMS_SENDER


class SmsLog(models.Model):
    sender = models.CharField(_('sender'), max_length=250, blank=True, default=DEFAULT_SMS_SENDER)
    number = models.CharField(_('number'), max_length=250)
    message_id = models.TextField(_('sender'), blank=True)
    message = models.TextField(_('message'))
    status = models.CharField(_('status'), max_length=20, default=SMS_STATUS_SUBMITTED)
    created_at = models.DateTimeField(_('created on'), default=timezone.now)
    updated_at = models.DateTimeField(_('updated on'), default=timezone.now)
    response = models.TextField(_('response'))  # Response from 3rd party server. e.g. Error Responses.


class SmsManager:

    def __init__(self):
        self.sender = None
        self.model = SmsLog

    def send(self, number, message, sender=None):
        self.sender = sender if sender else DEFAULT_SMS_SENDER
        return self.model.objects.create(sender=self.sender, number=number, message=message)

