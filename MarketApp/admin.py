from django.contrib import admin
from .models import  ItemDB

# Register your models here.



class itemAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'quantity','image_url']
    list_display=["title","description", 'quantity']
    
    

admin.site.register(ItemDB, itemAdmin)