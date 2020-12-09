from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from post.models import Post
from post.api.serializers import PostSerializers


@api_view(['GET'])
def api_details_post_view(request):
    try:
        post_data = Post.objects.get()

    except Post.DoesNotExits:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = PostSerializers(post_data)
        return Response(serializers.data)
