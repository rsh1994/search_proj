from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import search

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search, name='search'),
]
