from django.contrib import admin
from .models import Soru


# Register your models here.
class SoruAdmin(admin.ModelAdmin):
    list_display = ['sınıf', 'ders', 'konu', 'zorluk', 'slug', 'user', 'testid']
    list_display_links = ['sınıf', 'ders', 'konu', 'zorluk']
    list_filter = ['sınıf', 'ders', 'konu', 'zorluk']
    search_fields = []
    list_editable = []

    class Meta:
        model = Soru


admin.site.register(Soru, SoruAdmin)
