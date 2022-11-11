from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-created_at')
    context = {
        'articles':articles
    }
    return render(request, 'index.html', context)


def create_article(request):
    if request.method == 'GET':
        return render(request, 'create_article.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content, user=request.user)
        return redirect('community:index')