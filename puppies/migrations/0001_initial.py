# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Puppies'
        db.create_table(u'puppies_puppies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('litter', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('mother', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mother_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('mother_pedigree', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('mother_health', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('mother_titles', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('mother_training', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('father', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('father_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('father_pedigree', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('father_health', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('father_titles', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('father_training', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album'], null=True, blank=True)),
        ))
        db.send_create_signal(u'puppies', ['Puppies'])


    def backwards(self, orm):
        # Deleting model 'Puppies'
        db.delete_table(u'puppies_puppies')


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
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'father_health': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'father_pedigree': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'father_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'father_titles': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'father_training': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'litter': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mother_health': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'mother_pedigree': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_titles': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_training': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['puppies']