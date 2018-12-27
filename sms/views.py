from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from sms.serializers import SmsSerializer
from sms.models import SmsLog


class SmsList(generics.GenericAPIView):
    """
    List all sent sms or send a new sms. Send  a GET request to the endpoint /sms/ to receive the list of
    all sent SMS or send a POST request to the endpoint /sms/ with params: [number, message] to send a new
    SMS.
    """
    serializer_class = SmsSerializer
    queryset = SmsLog.objects.all()

    def get(self, request, format=None):
        data = SmsLog.objects.all()
        serializer = SmsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SmsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmsDetail(APIView):
    """
    Retrieve a single SMS
    """

    def get_object(self):
        id = self.request.query_params.get('id')

        # Try converting to integer to be sure a str was not sent by the user.
        try:
            id = int(id)
        except Exception:
            raise Http404

        try:
            return SmsLog.objects.get(pk=id)
        except SmsLog.DoesNotExist:
            raise Http404
        except Exception:
            raise Http404

    def get(self, request, format=None):
        sms = self.get_object()
        serializer = SmsSerializer(sms)
        return Response(serializer.data, status=status.HTTP_200_OK)
