from rest_framework import serializers

from userpost.models import UserPost, ShowPost


class ShowPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowPost
        fields = ['name', 'time']


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        # fields = ['id', 'user', 'title', 'time']
        fields = ['user_id', 'title', 'time', 'name']

        # def validate(self, data):
        #     u = data.get('title')
        #     print(u)
        #     return data
