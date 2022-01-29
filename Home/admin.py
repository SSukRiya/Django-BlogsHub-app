from django.contrib import admin

from .models import Notes, Domain
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display=('title', 'category', 'posted')

class DomainAdmin(admin.ModelAdmin):
    list_display=('domain',)

admin.site.register(Notes,NotesAdmin)
admin.site.register(Domain,DomainAdmin)