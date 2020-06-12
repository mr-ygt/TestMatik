from django.contrib import admin
from .models import Soru


# Register your models here.
class SoruAdmin(admin.ModelAdmin):
    list_display = ['title', 'sınıf', 'ders', 'konu', 'zorluk', 'slug', 'user', 'testid']
    list_display_links = ['sınıf', 'ders', 'konu', 'zorluk']
    list_filter = ['title', 'sınıf', 'ders', 'konu', 'zorluk']
    search_fields = ['title']
    list_editable = ['title']

    class Meta:
        model = Soru


admin.site.register(Soru, SoruAdmin)
