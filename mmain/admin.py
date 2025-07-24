from django.contrib import admin
from .models import Person,Car,Man,Business,Profile,Account
# Register your models here.
#admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Man)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Account)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age','hobby']
    search_fields = ['name']
    list_per_page = 5 
    list_display_links = ['name','hobby']
    ordering = ['age']
    list_editable = ['age']
    readonly_fields = ['name']
