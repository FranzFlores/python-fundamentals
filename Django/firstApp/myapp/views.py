from django.shortcuts import redirect, render, HttpResponse
from myapp.models import Article, Category
from django.db.models import Q
from myapp.forms import FormArticle
from django.contrib import messages

# Create your views here.

layout = """ 
    <h1> Sitio Web con  Django </h1>
    <hr> 
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/first_view/">Hello World</a></li>
        <li><a href="/page">Página de pruebas</a></li>
        <li><a href="/contact">Contacto</a></li>
    </ul>
    <hr>
    """


def index(request):
    variable = "Pollos Pollos Pollos"
    languages = ["Python", "JavaScript", "C++", "C#", "Java"]

    year = 2022
    interval = range(year, 2051)

    return render(request, 'index.html', {
        'name': 'Franz Flores',
        'title': 'Inicio',
        'languages': languages,
        'years': interval})


def first_view(request):
    return render(request, 'hello_world.html', {
        'list': ['Blue', 'Red', 'Green', 'Yellow']
    })


def page(request, redirect_page=0):
    if redirect_page == 1:
        return redirect("/")
    return render(request, 'page.html')

#  Con parametros en la URL


def contact(request, name="", lastname=""):
    html = ""

    if name and lastname:
        html += "El nombre completo es: "
        html += f"<h3>Contacto: {name} {lastname}</h3>"

    return HttpResponse(layout + f"""<h2>Contacto</h2>""" + html)


def create_article(request, title, content, public):
    article = Article(
        title=title,
        content=content,
        public=public,
        image="null"
    )

    article.save()

    return HttpResponse(f"Articulo creado: {article.title} - {article.content}")


def save_article(request):
    # Guardar un objeto en la BBDD por GET
    if request.method == 'POST':
        # Obtener por GET
        # title = request.GET.get('title') 
        # content = request.GET.get('content')
        # public = request.GET.get('public')

        title = request.POST.get('title')
        content = request.POST.get('content')
        public = request.POST.get('public')

        # if len(title) <= 5:
        #     return HttpResponse("<h1>El título debe tener más de 5 caracteres</h1>")

        article = Article(
            title=title,
            content=content,
            public=public
        )
        article.save()
        return HttpResponse(f"Articulo creado: {article.title} - {article.content}")
    else:
        return HttpResponse("<h1>No se encontro el articulo</h1>")
        

def create_article_form(request):
    return render(request, 'create_article.html')

def create_full_article(request):
    if request.method == 'POST':
        form_article = FormArticle(request.POST)

        if form_article.is_valid():
            data_form = form_article.cleaned_data

            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get('public')
            article = Article(
                title=title,
                content=content,
                public=public
            )
            article.save()

            #Crear mensaje Flash
            messages.success(request, f"Articulo creado: {article.title}")

            return redirect('get_articles')

    else:
        form_article = FormArticle()
    
    return render(request, 'create_full_article.html', {'form_article': form_article})



def get_article(request):
    # Sacar un solo objeto de la BBDD
    try:
        article = Article.objects.get(pk=2, public=False)
        response = f"Articulo: <br /> {article.title}"
    except:
        response = "<h1>No se encontro el articulo</h1>"

    return HttpResponse(response)


def update_article(request, id):
    try:
        article = Article.objects.get(pk=id)
        article.title = "Batman"
        article.content = "Pelicula de superheroes"
        article.save()
        response = f"Articulo actualizado: {article.title} - {article.content}"
    except:
        response = "<h1>No se encontro el articulo</h1>"

    return HttpResponse(response)


def get_articles(request):
    try:
        # articles = Article.objects.all() -> Todos los articulos
        articles = Article.objects.filter(public=True)
        # articles = Article.objects.order_by('title') -> Ordenar por titulo ascendente
        # articles = Article.objects.order_by('-title') -> Ordenar por titulo descendente
        # articles = Article.objects.order_by('title')[:1] -> Ordenar y limitar los elementos
        # articles = Article.objects.filter(title="prueba 2") -> Filtrar por titulo
        # articles = Article.objects.filter(title__contains="prueba") -> Filtrar por titulo que contenga "prueba"
        # articles = Article.objects.filter(title__exact="prueba") -> Filtrar por titulo que tenga exactamente "prueba"
        # articles = Article.objects.filter(title__iexact="prueba") -> Filtrar por titulo que tenga "prueba"
        # articles = Article.objects.filter(id__gte=3) -> Filtrar por id mayor o igual a 3
        # articles = Article.objects.filter(id__lte=3) -> Filtrar por id menor o igual a 3
        # articles = Article.objects.filter(title="prueba 2").exclude(public=False) -> Filtrar por titulo que tenga "prueba" y que no sea publico
        # articles = Article.objects.filter(Q(id__contains=2) | Q(title__contains="prueba")) -> Filtrar por id o titulo que contenga "prueba"

        # Consulta SQL pura
        # articles = Article.objects.raw(
        #     "SELECT * FROM myapp_article WHERE title = 'prueba 2' AND public = 1")

        return render(request, 'articles.html', {'articles': articles})
    except:
        return HttpResponse("<h1>Ocurrió un error al obtener los datos</h1>")


def delete_article(request, id):
    try:
        article = Article.objects.get(pk=id)
        article.delete()
        return redirect('/articles')
    except:
        return HttpResponse("<h1>Ocurrió un error al eliminar el artículo</h1>")
