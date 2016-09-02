from blog.models import Post
from api.serializers import PostSerializer
from rest_framework import viewsets, permissions


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
