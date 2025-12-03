from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User

# Create your views here.
@api_view(['POST'])
def signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')
    name = request.data.get('name')
    Preferred_language = request.data.get('Preferred_language')

    if password != confirm_password:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Passwords do not match'})
    user = User.objects.create(email=email, password=password, name=name, Preferred_language=Preferred_language)
    user.save()
    return Response(status=status.HTTP_201_CREATED, data={'message': 'Account created successfully'})