# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Puppies.gallery'
        db.alter_column(u'puppies_puppies', 'gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Puppies.gallery'
        raise RuntimeError("Cannot reverse this migration. 'Puppies.gallery' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Puppies.gallery'
        db.alter_column(u'puppies_puppies', 'gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album']))

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
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
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