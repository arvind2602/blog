from django.contrib import admin
from .models import category,post

# Register your models here.

class categoryadmin(admin.ModelAdmin):
    list_display=('category_id','title',)

class postadmin(admin.ModelAdmin):
    list_display=('post_id','title',)



admin.site.register(category,categoryadmin)
admin.site.register(post,postadmin)