from rest_framework import serializers
from .models import Movies


class MovieDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movies
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ('id', 'year', 'name', 'rate')