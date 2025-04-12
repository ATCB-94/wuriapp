from django.contrib import admin
from .models import AppelsOfrres, AMI
from .models import Contrat
from .models import Recrutement

# Register your models here.

class AppelsOffresAdmin(admin.ModelAdmin):
    list_display = ('titre', 'document', 'created_on', 'update_on')
    search_fields = ['titre']


class AMIAdmin(admin.ModelAdmin):
    list_display = ('titre', 'document', 'created_on', 'update_on')
    search_fields = ['titre']

class ContratAdmin(admin.ModelAdmin):
    list_display = ['libele']

class RecrutementAdmin(admin.ModelAdmin):
    list_display = ('titre','contrat_propose')
    list_display = ['titre']


admin.site.register(Contrat, ContratAdmin)
admin.site.register(AppelsOfrres, AppelsOffresAdmin)
admin.site.register(AMI, AMIAdmin)
admin.site.register(Recrutement, RecrutementAdmin)
