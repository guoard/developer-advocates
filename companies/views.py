from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer


@api_view()
def company_list(request):
    companies = Company.objects.prefetch_related('advocates').all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view()
def company_detail(request, id):
    company = Company.objects.get(pk=id)
    serializer = CompanySerializer(company)
    return Response(serializer.data)
