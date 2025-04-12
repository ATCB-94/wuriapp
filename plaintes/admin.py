from django.contrib import admin
from .models import Faq, glossaire, traitement, plainte;

# Register your models here.
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse', 'created_on', 'update_on')
    search_fields = ['question']

class glossaireAdmin(admin.ModelAdmin):
    list_display = ('mot', 'created_on', 'update_on')
    search_fields = ['mot']

class traitementAdmin(admin.ModelAdmin):
    list_display = ('titre', 'created_on', 'update_on')

class plainteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'objet', 'traitement', 'created_on')

admin.site.register(Faq, FaqAdmin)
admin.site.register(glossaire, glossaireAdmin)
admin.site.register(traitement, traitementAdmin)
admin.site.register(plainte, plainteAdmin)