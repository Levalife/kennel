# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Puppies.mother_title'
        db.add_column(u'puppies_puppies', 'mother_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.mother_training'
        db.add_column(u'puppies_puppies', 'mother_training',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.father_title'
        db.add_column(u'puppies_puppies', 'father_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.father_training'
        db.add_column(u'puppies_puppies', 'father_training',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


        # Changing field 'Puppies.mother_health'
        db.alter_column(u'puppies_puppies', 'mother_health', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'Puppies.mother_title'
        db.delete_column(u'puppies_puppies', 'mother_title')

        # Deleting field 'Puppies.mother_training'
        db.delete_column(u'puppies_puppies', 'mother_training')

        # Deleting field 'Puppies.father_title'
        db.delete_column(u'puppies_puppies', 'father_title')

        # Deleting field 'Puppies.father_training'
        db.delete_column(u'puppies_puppies', 'father_training')


        # Changing field 'Puppies.mother_health'
        db.alter_column(u'puppies_puppies', 'mother_health', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'puppies.puppies': {
            'Meta': {'object_name': 'Puppies'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'father_health': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'father_pedigree': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'father_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'father_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'father_training': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'litter': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mother_health': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'mother_pedigree': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_training': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['puppies']