from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from super_types import serializers
from super_types.models import SuperTypes
from .serializers import SuperTypesSerializer 

# Create your views here.
@api_view(['GET', 'POST'])
def supers_type_list(request):
    supers_types = SuperTypes.objects.all()
    if request.method == 'GET':
        supers_types = SuperTypes.objects.all()
        serializer = SuperTypesSerializer(supers_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':              #NO META DATA ERROR
        serializer = SuperTypesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_type_detail(request, pk):
    super_type = get_object_or_404(SuperTypes, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypesSerializer(super_type)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypesSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
