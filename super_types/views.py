from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from super_types import serializers
from super_types.models import SuperTypes
from .serializers import SuperTypesSerializer 

# Create your views here.
@api_view(['GET'])
def supers_type_list(request):
    supers_types = SuperTypes.objects.all()
    if request.method == 'GET':
        supers_types = SuperTypes.objects.all()
        serializer = SuperTypesSerializer(supers_types, many=True)
        return Response(serializer.data)
