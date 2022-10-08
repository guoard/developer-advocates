from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Company
from .serializers import CompanySerializer


class CompanyList(ListCreateAPIView):
    queryset = Company.objects.prefetch_related('advocates').all()
    serializer_class = CompanySerializer


class CompanyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.prefetch_related('advocates').all()
    serializer_class = CompanySerializer

    def delete(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        if company.advocates.count() > 0:
            return Response({'error': 'Company cannot be deleted because it is associated with advocates.'})
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
