from django.conf.urls import url, include
from api.views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
