

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from neighbour import serializers

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/users',
            'method':'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
        {
            'Endpoint':'/users/create',
            'method':'POST',
            'body': {'body':''},
            'description': 'Create new users'
        },
        {
            'Endpoint':'/users/update',
            'method':'PUT',
            'body': {'body':''},
            'description': 'Change data of users'
        },
        {
            'Endpoint':'/users/delete',
            'method':'DELETE',
            'body': None,
            'description': 'Delete user'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request,pk):
    user = User.objects.get(slug=pk)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request,pk):
    data = request.data
    user = User.objects.create(
        full_name=data['full_name'],
        slug=data['slug'],
        address=data['address'],
        telegram_id=data['telegram_id'],
        telegram_data=data['telegram_data']
    )
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

