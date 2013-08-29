# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dog.mother'
        db.add_column(u'dogs_dog', 'mother',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)

        # Adding field 'Dog.father'
        db.add_column(u'dogs_dog', 'father',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)


        # Changing field 'Dog.gallery'
        db.alter_column(u'dogs_dog', 'gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album'], null=True))

    def backwards(self, orm):
        # Deleting field 'Dog.mother'
        db.delete_column(u'dogs_dog', 'mother')

        # Deleting field 'Dog.father'
        db.delete_column(u'dogs_dog', 'father')


        # User chose to not deal with backwards NULL issues for 'Dog.gallery'
        raise RuntimeError("Cannot reverse this migration. 'Dog.gallery' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Dog.gallery'
        db.alter_column(u'dogs_dog', 'gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album']))

    models = {
        u'dogs.dog': {
            'Meta': {'object_name': 'Dog'},
            'about_dog': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'breeder': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'dm': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
            'hd': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mdr1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
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
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['dogs']