from django.contrib import admin
from .models import ImagePost,category,Location
# Register your models here.

class ImagePostAdmin(admin.ModelAdmin):
  filter_horizontal =('category',)

admin.site.register(Location)
admin.site.register(category)
admin.site.register(ImagePost, ImagePostAdmin)