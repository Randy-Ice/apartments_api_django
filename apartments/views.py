from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView, \
    UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Apartment, Comments
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import SimpleApartmentSerializer, DetailedApartmentSerializer, CommentsSerializer


# Create your views here.


class ApartmentView(ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = DetailedApartmentSerializer
    permission_classes = [IsAdminOrReadOnly]


class ApartmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = DetailedApartmentSerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)

