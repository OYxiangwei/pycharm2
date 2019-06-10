from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from case01.serializers import *
from case01.models import *

class studentvs(viewsets.ModelViewSet):
    serializer_class = studentser
    queryset = student.objects.all()
