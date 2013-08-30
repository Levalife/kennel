from django.contrib import admin
from models import Album, Image


from modeltranslation.admin import TranslationAdmin


class AlbumAdmin(TranslationAdmin):
    list_display = ["__unicode__", "images", "public"]
    
    class Media:
    	js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }        

class ImageAdmin(TranslationAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "album", "thumbnail","title", "created"]
    list_filter = ["album"]
    class Media:
    	js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)