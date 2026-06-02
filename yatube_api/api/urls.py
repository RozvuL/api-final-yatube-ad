from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

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
    path('jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
]
