"""firstApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

# Importar app con vistas
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('first_view/', views.first_view, name="first_view"),
    path('page/', views.page, name="page"),
    path('page/<int:redirect_page>', views.page, name="page"),
    #  Con parametros en la URL
    path('contact', views.contact, name="contact"),
    path('contact/<str:name>', views.contact, name="contact"),
    path('contact/<str:name>/<str:lastname>', views.contact, name="contact"),
    path('create-article/<str:title>/<str:content>/<str:public>', views.create_article, name="create_article"),
    path('get-article/', views.get_article, name="get_article"),
    path('update-article/<int:id>', views.update_article, name="update_article"),
    path('articles', views.get_articles, name="get_articles"),
    path('delete-article/<int:id>', views.delete_article, name="delete_article"),

    # Formualarios
    path('create-article-form/', views.create_article_form, name="create_article_form"),
    path('save-article/', views.save_article, name="save_article"),
    path('create-full-article',views.create_full_article, name="create_full_article"),
]

#Configuraciones para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)