from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status

import super_types 
from .serializers import SuperSerializer
from .models import Super
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])

def supers_list(request):
    supers = Super.objects.all()
    
    if type in request.GET and request.GET['hero']:
        hero = request.GET['hero']
        types = supers.filter(super_types__icontains='hero')
    elif type in request.GET and request.GET['hero']:
        villain = request.GET['villain']
        types = supers.filter(super_types__icontains='villain')
        context = {'super_type':super_types}
        return Response(request, context)
    elif request.method == 'GET':
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = supers.filter(super_type__lookup_name='villain')
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
