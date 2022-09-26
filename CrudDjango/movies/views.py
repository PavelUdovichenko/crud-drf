from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieDetailSerializer, MovieListSerializer
from .models import Movies
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieDetailSerializer


class MoviesListView(generics.ListAPIView):
    serializer_class = MovieListSerializer
    queryset = Movies.objects.all()
    permission_classes = (IsAuthenticated, )


class MoviesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movies.objects.all()
    # authentication_classes = (TokenAuthentication, SessionAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser, )
