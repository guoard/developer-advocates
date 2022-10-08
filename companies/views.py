from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Company
from advocates.models import Advocate
from .serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.prefetch_related('advocates').all()
    serializer_class = CompanySerializer

    def destroy(self, request, *args, **kwargs):
        if Advocate.objects.filter(company_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Company cannot be deleted because it is associated with advocates.'})

        return super().destroy(request, *args, **kwargs)
