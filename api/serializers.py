from rest_framework import serializers
from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text', 'created_date', 'published_date', 'comments')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_date', 'approved_comment',)
