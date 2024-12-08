from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titre_court', 'statut', 'created_on', 'update_on' )
    list_filter = ('statut',)
    search_fields = ['titre_court', 'contenu']

admin.site.register(Post, PostAdmin)