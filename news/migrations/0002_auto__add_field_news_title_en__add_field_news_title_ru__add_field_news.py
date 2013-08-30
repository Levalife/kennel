# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.title_en'
        db.add_column(u'news_news', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.title_ru'
        db.add_column(u'news_news', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.body_en'
        db.add_column(u'news_news', 'body_en',
                      self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.body_ru'
        db.add_column(u'news_news', 'body_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.title_en'
        db.delete_column(u'news_news', 'title_en')

        # Deleting field 'News.title_ru'
        db.delete_column(u'news_news', 'title_ru')

        # Deleting field 'News.body_en'
        db.delete_column(u'news_news', 'body_en')

        # Deleting field 'News.body_ru'
        db.delete_column(u'news_news', 'body_ru')


    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'body_en': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'body_ru': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 30, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']