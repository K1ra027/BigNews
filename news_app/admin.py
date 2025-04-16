from django.contrib import admin
from .models import Category, News
# Register your models here.




admin.site.register(Category)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_at']
    list_display_links = ['created_at','title']
    list_filter = ['category','created_at']
    search_fields = ['title']



