from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocate
from .serializers import AdvocateSerializer


@api_view()
def advocate_list(request):
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)


@api_view()
def advocate_detail(request, id):
    advocate = Advocate.objects.get(pk=id)
    serializer = AdvocateSerializer(advocate)
    return Response(serializer.data)
