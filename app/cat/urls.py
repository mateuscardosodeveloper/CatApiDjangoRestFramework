from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cat import views

router = DefaultRouter()
router.register('cat', views.CatViewSet)

app_name = 'cat'

urlpatterns = [
    path('', include(router.urls))
]
