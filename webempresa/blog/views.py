from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Category

def blog(request):
    # Obtener todos los posts
    posts = Post.objects.all()

    # Paginar los posts
    paginator = Paginator(posts, 3)  # 1 post por p�gina, ajusta esto seg�n tus necesidades
    page_number = request.GET.get('page')  # Obtener el n�mero de p�gina desde la URL
    try:
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el n�mero de p�gina no es un entero, mostrar la primera p�gina
        return render(request, "blog/404.html")
    except EmptyPage:
        # Si la p�gina est� fuera de rango (por ejemplo, 9999), mostrar la �ltima p�gina
        return render(request, "blog/404.html")

    return render(request, "blog/blog.html", {'posts': paginated_posts})


def category(request, category_id):
    # Obtener la categoría especificada
    category = get_object_or_404(Category, id=category_id)

    # Obtener todos los posts de la categoría especificada
    posts_in_category = Post.objects.filter(categories=category)

    # Paginar los posts de la categoría
    paginator = Paginator(posts_in_category, 3)  # 3 posts por página, ajusta según tus necesidades
    page_number = request.GET.get('page')  # Obtener el número de página desde la URL
    try:
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la primera página
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, "blog/category.html", {'category': category, 'posts': paginated_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/detail.html", {'post': post})
