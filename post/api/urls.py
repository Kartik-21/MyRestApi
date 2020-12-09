from django.urls import path

from post.api.views import api_details_post_view, api_update_post_view, api_create_post_view, api_delete_post_view

urlpatterns = [
    path(r'view/', api_details_post_view),
    path(r'update/', api_update_post_view),
    path(r'create/', api_create_post_view),
    path(r'delete/', api_delete_post_view),
]
