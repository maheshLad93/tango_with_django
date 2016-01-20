from django.contrib import admin

# Register your models here.

from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Page)