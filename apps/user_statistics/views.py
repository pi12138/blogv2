# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserIP, UserInterviewInfo
import datetime
# Create your views here.


@api_view(http_method_names=['GET'])
def interview_count(request):
    """
    访问数量统计
    """
    users = UserIP.objects.all()
    
    if not users.exists():
        return Response({'count': 0})

    count = sum([user.count for user in users])

    return Response({'count': count})


@api_view(http_method_names=['GET'])
def article_read_count(request):
    """
    文章的访问数量
    """
    article = request.query_params.get('article', "")

    if not article:
        return Response("为传入文章ID")

    path = "/blogv2/articles/{}/".format(article)

    users = UserInterviewInfo.objects.filter(interview_url=path)
    
    return Response({'count': users.count()})

@api_view(http_method_names=['GET'])
def one_day_visits(request):
    """
    一天的访问量
    """
    date = request.query_params.get('date')

    if not date:
        # 未传入时间，默认为当前时间
        date = datetime.datetime.now()
        date = date.strftime('%Y-%m-%d')
    year, month, day = date.split('-')
    users = UserInterviewInfo.objects.filter(interview_time__year=year, interview_time__month=month, interview_time__day=day)
    
    return Response({'count': users.count()})