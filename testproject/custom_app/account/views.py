from account import serializers
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from plugins import public as plugin_public
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import authentication
# Create your views here.


class UseSignUp(generics.CreateAPIView):
    """Class for user sign up."""

    permission_classes = ()
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            plugin_public.get_tokens_for_user(user),
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )


class UserSignIn(APIView):
    """Class for user sign in."""

    permission_classes = ()
    serializer_class = serializers.UserSerializer
    def post(self, request,):
        data = request.data
        if not data.get('email'):
            return Response({'error': 'e-mail missing'})

        password = data.get('password')
        validate = authentication.authenticate
        user = validate(username=data['email'], password=password)
        if not user:
            return Response({'error': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(plugin_public.get_tokens_for_user(user), status=status.HTTP_200_OK)

