from .models import SmsLog
from rest_framework import serializers


class SmsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = SmsLog
        fields = ('id', 'sender', 'number', 'message', 'status', 'created_at')
