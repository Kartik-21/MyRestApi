from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from post.api.views import api_details_post_view, api_update_post_view, api_create_post_view, api_delete_post_view

urlpatterns = [
    path(r'view/', api_details_post_view),
    path(r'update/<int:pk>/', api_update_post_view),
    path(r'create/', api_create_post_view),
    path(r'delete/<int:pk>/', api_delete_post_view),
]
