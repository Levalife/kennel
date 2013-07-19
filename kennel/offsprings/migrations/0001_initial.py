# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Offspring'
        db.create_table(u'offsprings_offspring', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('mother', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('father', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('sex', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dogs.Gender'])),
            ('birthday', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('pedigree', self.gf('django.db.models.fields.URLField')(max_length=150, blank=True)),
            ('hd', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('mdr1', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('dm', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('titles', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('training', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('about_dog', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photogallery.Album'])),
        ))
        db.send_create_signal(u'offsprings', ['Offspring'])


    def backwards(self, orm):
        # Deleting model 'Offspring'
        db.delete_table(u'offsprings_offspring')


    models = {
        u'dogs.gender': {
            'Meta': {'object_name': 'Gender'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'offsprings.offspring': {
            'Meta': {'object_name': 'Offspring'},
            'about_dog': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'dm': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photogallery.Album']"}),
            'hd': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mdr1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'pedigree': ('django.db.models.fields.URLField', [], {'max_length': '150', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sex': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Gender']"}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'training': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        u'photogallery.album': {
            'Meta': {'ordering': "['title']", 'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['offsprings']