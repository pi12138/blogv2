from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view
from . import serializers
from . import models
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    """
    文章视图
    """
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    @action(methods=['get'], detail=False)
    def search_article(self, request):
        """搜索文章"""
        keyword = request.query_params.get('keyword', "")

        if not keyword:
            return Response("未传入关键字！")

        articles = self.queryset.filter(Q(title__icontains=keyword)|Q(category__icontains=keyword))
        ser = serializers.IndexSerializer(instance=articles, many=True)

        return Response(ser.data)

    @action(methods=['get'], detail=False)
    def similar_article(self, request):
        """相似的文章"""
        category = request.query_params.get('category', "")

        if not category:
            return Response("未传入分类！")

        articles = self.queryset.filter(Q(title__icontains=category)|Q(category__icontains=category))[0:10]
        ser = serializers.IndexSerializer(instance=articles, many=True)

        return Response(ser.data)


class IndexViewSet(viewsets.ModelViewSet):
    """
    主页
    """
    queryset = models.Article.objects.all()
    serializer_class = serializers.IndexSerializer

    @action(methods=['get'], detail=False)
    def commented_article(self, request):
        """近期被评论过的文章"""
        articles = self.queryset.filter(comment__content__isnull=False).order_by('-comment__pub_date')[:5]
        article_dict = {}
        for article in articles:
            if article.id not in article_dict:
                article_dict[article.id] = article.title
            else:
                pass

        return Response(article_dict)


class ArticleCategoryViewSet(viewsets.ModelViewSet):
    """
    博客标签
    """
    queryset = models.ArticleCategory.objects.all()
    serializer_class = serializers.ArticleCategorySerializer

    @action(methods=['get'], detail=False)
    def same_category(self, request):
        """
        每个标签的文章数
        """
        categorys = self.get_queryset()

        category_list = list()
        for category in categorys:
            article_num = category.article_set.all().count()

            category_info = (category.id, category.name, article_num)
            category_list.append(category_info)

        return Response(category_list)

    @action(methods=['get'], detail=False)
    def search_articles_from_category(self, request):
        """
        根据标签查询文章
        """
        category_id = request.query_params.get('category_id', "")

        if not category_id:
            return Response("未传入标签ID")

        category = models.ArticleCategory.objects.filter(id=category_id)

        if not category.exists():
            return Response("该文章分类不存在")

        articles = category[0].article_set.all()

        ser = serializers.ArticleSerializer(instance=articles, many=True)

        return Response(ser.data)


class ArticleArchiveView(views.APIView):
    """
    文章按日期归档
    """
    def get(self, request, *args, **kwargs):
        """
        文章按照日期归档
        """
        dateinfo = request.query_params.get("dateinfo", "")
        if not dateinfo:
            data_list = self.get_article_archive()
            
            return Response(data_list)
        else:
            article_list = self.get_articles_from_dateinfo(dateinfo)
            
            return Response(article_list)
        
        return Response("error")

    def get_article_archive(self):
        """
        获取所有的日期分组，以及每个分组后的文章数目
        return: [(date, count),...]
        """
        dates = models.Article.objects.dates('update_time', 'month', order='DESC')

        date_list = list()
        for date in dates:
            date_str = date.strftime("%Y-%m")
            year, month = date_str.split('-')
            count = models.Article.objects.filter(update_time__year=year, update_time__month=month).count()
            date_list.append((date_str, count))
        
        return date_list

    def get_articles_from_dateinfo(self, dateinfo):
        """
        根据传入的日期信息，返回文章列表
        return: [article_obj, ......]
        """
        year, month = dateinfo.split("-")

        articles = models.Article.objects.filter(update_time__year=year, update_time__month=month)

        ser = serializers.IndexSerializer(instance=articles, many=True)
      
        return ser.data


