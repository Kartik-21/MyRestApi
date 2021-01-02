from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from userpost.api.views import api_details_post_view, api_update_post_view, api_create_post_view, api_delete_post_view, \
    UserPostAPIView, UserPostCUDAPIView, ShowPostList, LCUserPost, RUDUserPost

urlpatterns = [
    path(r'view/', api_details_post_view),
    path(r'update/<int:pk>/', api_update_post_view),
    path(r'create/', api_create_post_view),
    path(r'delete/<int:pk>/', api_delete_post_view),
    path(r'v2/view/', UserPostAPIView.as_view()),
    path(r'v2/update/<int:id>/', UserPostCUDAPIView.as_view()),
    path(r'v2/showpost/', ShowPostList.as_view()),
    path(r'v3/api_lc/', LCUserPost.as_view()),
    path(r'v3/api_rud/<int:id>/', RUDUserPost.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
