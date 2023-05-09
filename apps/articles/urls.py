from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, 'articles')

urlpatterns = router.urls