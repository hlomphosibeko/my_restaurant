from django.contrib import admin
from .models import Menu, Category, CustomerComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    list_display = ('menu_title', 'slug')
    search_fields = ['menu_title']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('menu_title',)}
    summernote_fields = ('text',)


# Register your models here.
admin.site.register(Category)
admin.site.register(CustomerComment)
