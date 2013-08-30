# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Album.title_en'
        db.add_column(u'gallery_album', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Album.title_ru'
        db.add_column(u'gallery_album', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Image.title_en'
        db.add_column(u'gallery_image', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Image.title_ru'
        db.add_column(u'gallery_image', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Album.title_en'
        db.delete_column(u'gallery_album', 'title_en')

        # Deleting field 'Album.title_ru'
        db.delete_column(u'gallery_album', 'title_ru')

        # Deleting field 'Image.title_en'
        db.delete_column(u'gallery_image', 'title_en')

        # Deleting field 'Image.title_ru'
        db.delete_column(u'gallery_image', 'title_ru')


    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']