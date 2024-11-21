from django.shortcuts import render
from rest_framework import viewsets
from.serializers import *
from.models import *

class ProductViewset(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()


class CommentViewset(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
