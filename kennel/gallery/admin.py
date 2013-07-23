from django.contrib import admin
from models import Album, Image

class AlbumAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "images", "public"]

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "album", "thumbnail","title", "created"]
    list_filter = ["album"]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)