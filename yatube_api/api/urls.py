from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/follow/',
         FollowViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/', include('djoser.urls.jwt')),
]
