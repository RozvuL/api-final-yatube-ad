from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('groups', views.GroupViewSet)
router.register('follow', views.FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('jwt/', include('djoser.urls.jwt')),
]