from django.contrib import admin

from presentation.models import Partenaire, Entreprise, Objectif, Service, Realisation, Team


class EntrepriseAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Vérifie si un centre existe déjà
        if Entreprise.objects.exists():
            return False  # Désactive l'ajout d'un nouveau centre
        return True

    list_display = ['nom', 'description', 'adresse', 'slogan']


class ObjectifAdmin(admin.ModelAdmin):
    list_display = ('objectif', 'date_add', 'date_modif')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image', 'date_add', 'date_modif')


class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sigle', 'adresse', 'pays', 'ville', 'image', 'date_add', 'date_modif')
    list_filter = ('pays', 'ville')
    search_fields = ('nom', 'sigle')


admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(Objectif, ObjectifAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Team)
admin.site.register(Realisation)
admin.site.register(Partenaire, PartenaireAdmin)