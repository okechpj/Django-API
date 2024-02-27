from rest_framework.decorators import api_view
from .serializers import UserSerializer, OneUser
from user_data.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView


# class based view for a post and get request
class ApiUser(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

 

# function based view for get, put and delete requests
@api_view(['GET', 'PUT', 'DELETE'])
def one_user_api(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'GET':
        serializer = OneUser(user)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method == 'DELETE':
        user.delete()
        return Response("Item deleted Successfully!", status=status.HTTP_204_NO_CONTENT)