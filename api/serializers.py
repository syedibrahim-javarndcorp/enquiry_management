from rest_framework import serializers
from ems.models import Ems, Tag
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class EmsSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tag = TagSerializer(many=True)

    class Meta:
        model = Ems
        fields = '__all__'
