import string
import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for i in range(length))
    return random_string


class LoginAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            self.validate_username(username)
            self.validate_password(password)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        user = self.authenticate(username, password);

        if user is not None:
            token = generate_random_string(16);
            return Response({
                'token': token
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def validate_username(self, username):
        if not username:
            raise ValidationError("Username is required.")

        # Add input sanitisation logic here

        return True

    def validate_password(self, password):
        if not password:
            raise ValidationError("Password is required.")
        # Add input sanitisation logic here
        return True

    def authenticate(self, username, password):

        if username == "Hexaware" and password == "hexawareuk":
            return 'Login Successful';

        return None;


