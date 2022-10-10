from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Advocate
from .serializers import AdvocateSerializer, CreateAdvocateSerializer


class AdvocateViewSet(ModelViewSet):
    allow_http_methods = ['get', 'post', 'put', 'delete']

    def update(self, request, *args, **kwargs):
        serializer = CreateAdvocateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        advocate = serializer.save()
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)

    queryset = Advocate.objects.select_related(
        'company').prefetch_related('links').all()

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return CreateAdvocateSerializer
        return AdvocateSerializer
