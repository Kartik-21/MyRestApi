from rest_framework import serializers

from userpost.models import UserPost


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        # fields = ['id', 'user', 'title', 'time']
        fields = ['user_id', 'title', 'time']
