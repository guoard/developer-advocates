from rest_framework.viewsets import ModelViewSet

from .models import Advocate
from .serializers import AdvocateSerializer, AddAdvocateSerializer


class AdvocateViewSet(ModelViewSet):
    queryset = Advocate.objects.select_related(
        'company').prefetch_related('links').all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddAdvocateSerializer
        return AdvocateSerializer
