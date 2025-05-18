from rest_framework import serializers

from apartments.models import Apartment, Activities, Comments, PointsOfInterests, Address, Note


class PointsOfInterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsOfInterests
        fields = 'id', 'name'
class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = 'id', 'name'

class SimpleApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = [
            'id', 'name', 'description', 'price', 'image'
        ]

class DetailedApartmentSerializer(serializers.ModelSerializer):
    points_of_interests = serializers.StringRelatedField(many=True, read_only=True)
    activities = serializers.StringRelatedField(many=True, read_only=True)
    class Meta(SimpleApartmentSerializer.Meta):
        model = Apartment
        fields = SimpleApartmentSerializer.Meta.fields + [
            'address','number_of_beds','baths','pets_allowed',
            'home_type','square_feet','contact','activities',
            'points_of_interests','created_at','updated_at',

        ]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id',
            'apartment',
            'name',
            'description',
            'created_at',
        ]
        read_only_fields = ['created_at', "name"]

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'location']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['apartment', 'description']