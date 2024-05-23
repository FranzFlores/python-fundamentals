from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    #Mostrar los campos de solo lectura
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configuar el titlo del panel
title = "Administración de Artículos"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión"

