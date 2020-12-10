from rest_framework import serializers

from post.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['id', 'user', 'title', 'time']
        fields = ['user_id', 'title', 'time']
