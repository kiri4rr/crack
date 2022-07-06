from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cracker
from .models import User
# Create your views here.
from .serializers import CrackerSerializer
from .serializers import UserSerializer


class CrackerAPIView(APIView):
    def get(self, request):
        l = Cracker.objects.all()
        return Response({'questions': CrackerSerializer(l, many=True).data})

    def post(self, request):
        serializer = CrackerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class UserAPIView(APIView):
    def get(self, request):
        ls = User.objects.all()
        return Response({'gets': UserSerializer(ls, many=True).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


# class CrackerAPIView(generics.ListAPIView):
#    queryset = Cracker.objects.all()
#    serializer_class = CrackerSerializer
