from django.contrib import admin
from .models import ImagePost,category,Location
# Register your models here.

admin.site.register(Location)
admin.site.register(category)
admin.site.register(ImagePost)