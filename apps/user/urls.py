from django.urls import include, path

from .views import ProfileViewSet, SharedMe


urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('user/<int:id>/profile/', ProfileViewSet.as_view({
        'get': 'retrieve', })),
    path('user/me/profile/', ProfileViewSet.as_view({
        'put': 'me',
        'patch': 'me', })),
    path('user/me/shared/', SharedMe.as_view()),
]