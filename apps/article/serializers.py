from .models import Article, ArticleCategory
from rest_framework import serializers
from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField(method_name="get_comment")
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'category', 'category_name', 'pub_date', 'update_time', 'content', 'comment')
        extra_kwargs = {'category': {'write_only': True}}

    def get_comment(self, obj):
        comments = Comment.objects.filter(article_id=obj.id)
        ser = CommentSerializer(instance=comments, many=True)
        return ser.data


class IndexSerializer(serializers.ModelSerializer):
    article_url = serializers.CharField(read_only=True)
    category_name = serializers.CharField(read_only=True)
    update_time_handler = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'category_name', 'update_time_handler', 'article_url')
        extra_kwargs = {'title': {'read_only': True}}


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"

