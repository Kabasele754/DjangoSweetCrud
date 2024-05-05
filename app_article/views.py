from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.http import JsonResponse, HttpResponse


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)  # Paginate les articles par 10 par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app_article/article_list.html', {'page_obj': page_obj})

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article

def show_article_details(request, pk):
    article = get_object_or_404(Article, pk=pk)
    data = {
        'id': article.id,
        'title': article.title,
        'description': article.description,
        'image': article.image.url if article.image else None
    }
    return JsonResponse({'success': True, 'article': data})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            # Récupérer les données nécessaires pour mettre à jour la vue
            data = {
                'success': True,
                'message': f'Article "{article.title}" created successfully.',
                'id': article.id,
                'title': article.title,
                'description': article.description,
                'image': article.image.url if article.image else None
            }
            return JsonResponse(data, encoder=DjangoJSONEncoder)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = ArticleForm()
    return render(request, 'app_article/article_form.html', {'form': form})


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            data = {
                'success': True,
                'message': f'Article "{article.title}" updated successfully.',
                'id': article.id,
                'title': article.title,
                'description': article.description,
                'image': article.image.url if article.image else None
            }
            return JsonResponse(data, encoder=DjangoJSONEncoder)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'app_article/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        # Ajoutez ici la logique de suppression de l'élément
        article.delete()
        return HttpResponse(status=204)  # Réponse HTTP 204 No Content (success)

    return HttpResponse(status=400)  # Réponse HTTP 400 Bad Request (erreur)
