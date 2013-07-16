# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Dog.about_dog'
        db.alter_column(u'dogs_dog', 'about_dog', self.gf('django.db.models.fields.TextField')(max_length=400))

        # Changing field 'Dog.titles'
        db.alter_column(u'dogs_dog', 'titles', self.gf('django.db.models.fields.TextField')(max_length=400))

    def backwards(self, orm):

        # Changing field 'Dog.about_dog'
        db.alter_column(u'dogs_dog', 'about_dog', self.gf('django.db.models.fields.CharField')(max_length=400))

        # Changing field 'Dog.titles'
        db.alter_column(u'dogs_dog', 'titles', self.gf('django.db.models.fields.CharField')(max_length=400))

    models = {
        u'dogs.dog': {
            'Meta': {'object_name': 'Dog'},
            'about_dog': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'breeder': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'dm': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photogallery.Album']"}),
            'hd': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mdr1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'pedigree': ('django.db.models.fields.URLField', [], {'max_length': '150', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sex': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Gender']"}),
            'titles': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'training': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        u'dogs.gender': {
            'Meta': {'object_name': 'Gender'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'photogallery.album': {
            'Meta': {'ordering': "['title']", 'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['dogs']