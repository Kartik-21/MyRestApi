from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from userpost.models import UserPost
from userpost.api.serializers import PostSerializers


@api_view(['GET'])
def api_details_post_view(request):
    data = {}
    try:
        post_data = UserPost.objects.all()

    except UserPost.DoesNotExist:
        data["msg"] = "object not found"
        # return 404 http response
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # if multiple data then true many property
        serializers = PostSerializers(post_data, many=True)
        # if we want return json data => JsonResponse
        # if we want return api page => Response
        return JsonResponse(serializers.data, safe=False)


@api_view(['PUT'])
def api_update_post_view(request, pk):
    data = {}
    try:
        # pk is db primary key of that table
        post_data = UserPost.objects.get(pk=pk)

    except UserPost.DoesNotExist:
        data["msg"] = "object not found"
        return JsonResponse(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        # it is used for fetch data from the api
        data1 = JSONParser().parse(request)
        serializers = PostSerializers(post_data, data=data1)
        if serializers.is_valid():
            serializers.save()
            data["msg"] = "update successful"
        else:
            data["msg"] = status.HTTP_400_BAD_REQUEST

        return JsonResponse(data=data)


@api_view(['POST'])
def api_create_post_view(request):
    # account = Post.objects.get()
    # p = Post(user=account)

    if request.method == "POST":
        serializer = PostSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["msg"] = "Post Created"
        else:
            data["msg"] = status.HTTP_400_BAD_REQUEST

        return JsonResponse(data=data)


@api_view(['DELETE'])
def api_delete_post_view(request, pk):
    data = {}
    try:
        post_data = UserPost.objects.get(pk=pk)
    except UserPost.DoesNotExist:
        data["msg"] = "object not found"
        return JsonResponse(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = post_data.delete()
        if operation:
            data["msg"] = "delete successful"
        else:
            data["msg"] = "delete failed"

        return JsonResponse(data=data)
