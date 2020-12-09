from django.urls import path

from post.api.views import api_details_post_view

app_name = 'post'

urlpatterns = [
    path('', api_details_post_view, name='detail'),
]
