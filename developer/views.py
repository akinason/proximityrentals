from django.http import Http404

from rest_framework import generics, status, permissions
from rest_framework.response import Response

from developer.serializers import AppSerializer 
from developer.models import App 
from developer.permissions import HasAPISuperAccess

class AppList(generics.GenericAPIView):
    """
    Responsible for creating new application keys or getting the list of existing API keys belonging to 
    the request.user
    """
    serializer_class = AppSerializer
    model = App 
    permission_classes = (permissions.IsAuthenticated, HasAPISuperAccess)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.user = request.user
        serializer.context['request'] = request
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        querset = self.model.objects.filter(is_deleted=False, user=self.request.user)
        return querset

    def get(self, request, format=None):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppDetail(generics.GenericAPIView):
    """
    Get the details of an app.
    """
    model = App 
    serializer_class = AppSerializer
    permission_classes = (permissions.IsAuthenticated, HasAPISuperAccess)

    def get_object(self):
        id = self.request.query_params.get('id') or self.request.POST.get('id')

        try:
            obj = self.model.objects.filter(is_deleted=False).get(pk=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except self.model.DoesNotExist:
            raise Http404
        except Exception:
            raise Http404

    def get(self, request, format=None):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)