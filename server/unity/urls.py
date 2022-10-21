from django.urls import include, path 
from rest_framework.routers import DefaultRouter
from .views import (
    UserCreateAPIView, UserListAPIView, UserCountAPIView
)

router = DefaultRouter()
urlpatterns = [
    path('api/', include([
        path('users', UserCreateAPIView.as_view(), name='user-create'),
        path('users/', UserListAPIView.as_view(), name='user-get-many'),
        path('users/count/', UserCountAPIView.as_view(), name='user-get-count'),
    ])),
]

