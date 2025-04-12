from django.contrib import admin
from .models import Activite
from .models import Image
from .models import Document
from .models import Video, Publication_media

# Register your models here.
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('libele', 'date', 'created_on', 'update_on' )
    search_fields = ['libele']

class ImageAdmin(admin.ModelAdmin):
    list_display = ('activite', 'image', 'created_on', 'update_on' )

class VideoAdmin(admin.ModelAdmin):
    list_display = ('activite', 'video', 'created_on', 'update_on' )


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('libele', 'activite', 'media', 'created_on', 'update_on' )

class Publication_mediaAdmin(admin.ModelAdmin):
    list_display = ('libele', 'url_media', 'created_on', 'update_on' )


admin.site.register(Activite, ActiviteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Publication_media, Publication_mediaAdmin)