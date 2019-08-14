from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.article.models import Article
import json
# Create your views here.


def article(request):
    return render(request, 'article.html')


def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def test_json(request):
    print(request.POST)
    print(request.method)
    print(request.body)
    data = json.loads(request.body.decode())
    print("data:", data)
    print("data type:", type(data))
    # return HttpResponse("xxxxx")
    return JsonResponse(json.dumps(data), safe=False)


def test_add(request):
    arts = Article.objects.all()
    art_title_list = [art.title for art in arts]
    print("len arts:", len(arts))

    art = Article()

    if "xxxxx" not in art_title_list:
        art.title = 'xxxxx'
        art.category = 'xxxx'
        art.content = 'xxxx'

        art.save()

    arts = Article.objects.all()

    print("len arts:", len(arts))

    return HttpResponse('ok', reason="xxxxx")


def test_response(request):
    response = HttpResponse("test_response")

    print(response.items())
    print(response.getvalue())

    return response