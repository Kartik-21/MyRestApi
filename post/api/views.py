from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from post.models import Post
from post.api.serializers import PostSerializers


@api_view(['GET'])
def api_details_post_view(request):
    try:
        post_data = Post.objects.get(pk=1)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = PostSerializers(post_data)
        return Response(serializers.data)


@api_view(['PUT'])
def api_update_post_view(request):
    try:
        post_data = Post.objects.get()

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializers = PostSerializers(post_data)
        data = {}
        if serializers.is_valid():
            serializers.save()
            data["msg"] = "update successful"
        else:
            data["msg"] = status.HTTP_400_BAD_REQUEST

        return Response(data=data)


@api_view(['POST'])
def api_create_post_view(request):
    account = Post.objects.get(pk=1)
    p = Post(user=account)

    if request.method == "POST":
        serializer = PostSerializers(p, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["msg"] = status.HTTP_201_CREATED
        else:
            data["msg"] = status.HTTP_400_BAD_REQUEST

        return Response(data=data)


@api_view(['DELETE'])
def api_delete_post_view(request):
    try:
        post_data = Post.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = post_data.delete()
        data = {}
        if operation:
            data["msg"] = "delete successful"
        else:
            data["msg"] = "delete failed"

        return Response(data=data)
