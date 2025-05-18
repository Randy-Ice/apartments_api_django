from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, \
     ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Apartment, Note, Address, Activities, PointsOfInterests, Comments
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import DetailedApartmentSerializer, CommentsSerializer, NoteSerializer, PointsOfInterestsSerializer, \
    AddressSerializer, ActivitiesSerializer


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

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAdminOrReadOnly]

class PointsOfInterestsViewSet(viewsets.ModelViewSet):
    queryset = PointsOfInterests.objects.all()
    serializer_class = PointsOfInterestsSerializer
    permission_classes = [IsAdminOrReadOnly]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdminOrReadOnly]

class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [IsAdminOrReadOnly]

