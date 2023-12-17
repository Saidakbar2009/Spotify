from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albom', AlbomModelViewSet)
router1 = DefaultRouter()
router1.register(r'qoshiqchi', QoshiqchiModelViewSet)
router2 = DefaultRouter()
router2.register(r'qoshiq', QoshiqModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('', include(router2.urls)),
]
