
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from developer.models import App
from main.models import User

class AppSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(allow_blank=False, required=True)
    key = serializers.CharField(read_only=True, allow_null=True)
    secret = serializers.CharField(read_only=True, allow_null=True)
    is_active = serializers.BooleanField(read_only=True)
    created_on = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True, is_deleted=False), required=False)

    class Meta:
        model = App 
        fields = ('id', 'name', 'key', 'secret', 'is_active', 'created_on', 'user')
    

    def create(self, validated_data):
        obj = super(AppSerializer, self).create(validated_data)
        obj.set_keys()
        obj.user = self.context['request'].user
        obj.save()
        return obj