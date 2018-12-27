import datetime
from proximityrentals import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION


class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False

    def get_available_name(self, name, max_length=None):
        custom_name = '%s%s%s' % (datetime.date.today(), '/', name)
        return super().get_available_name(custom_name, max_length)


class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    file_overwrite = False
    default_acl = 'private'
    custom_domain = False

    def get_available_name(self, name, max_length=None):
        custom_name = '%s%s%s' % (datetime.date.today(), '/', name)
        return super().get_available_name(custom_name, max_length)
