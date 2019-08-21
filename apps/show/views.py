from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.article.models import Article
import json
# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def article(request, pk):
    return render(request, 'article.html', {'pk': pk})

def index(request):
    return render(request, 'index.html')

def search(request):
    kw = request.POST.get('keyword', "")
    return render(request, 'search.html', {'keyword': kw})

def archive(request):
    return render(request, 'archive.html')

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


@csrf_exempt
def upload_file(request):
    """
    測試上傳文件到阿里雲oss
    """
    if request.method == "GET":
        return render(request, 'upload_file.html')
    elif request.method == "POST":
        from apps.upload_file.helper import QiniuOSS

        file = request.FILES['file']

        bucket = "upload"

        oss = QiniuOSS(bucket)
        oss.upload_file(file)        
        
        return HttpResponse("ok")