from django.shortcuts import render,redirect,get_object_or_404
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


def article_detail(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        context = {
            'article': article,
        }
        return render(request, 'article_detail.html', context)


def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        context = {
            'article': article
        }
        return render(request, 'update_article.html', context) 
    
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('community:article_detail', article_id)


def delete_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        if request.user != article.user:
            return HttpResponse('권한이 없습니다. error=403')
        else:
            article.delete()
            return redirect('community:index')