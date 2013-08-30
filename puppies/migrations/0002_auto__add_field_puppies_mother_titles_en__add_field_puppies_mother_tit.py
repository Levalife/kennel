# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Puppies.mother_titles_en'
        db.add_column(u'puppies_puppies', 'mother_titles_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.mother_titles_ru'
        db.add_column(u'puppies_puppies', 'mother_titles_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.mother_training_en'
        db.add_column(u'puppies_puppies', 'mother_training_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.mother_training_ru'
        db.add_column(u'puppies_puppies', 'mother_training_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.father_titles_en'
        db.add_column(u'puppies_puppies', 'father_titles_en',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.father_titles_ru'
        db.add_column(u'puppies_puppies', 'father_titles_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.father_training_en'
        db.add_column(u'puppies_puppies', 'father_training_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.father_training_ru'
        db.add_column(u'puppies_puppies', 'father_training_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.amount_en'
        db.add_column(u'puppies_puppies', 'amount_en',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Puppies.amount_ru'
        db.add_column(u'puppies_puppies', 'amount_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Puppies.mother_titles_en'
        db.delete_column(u'puppies_puppies', 'mother_titles_en')

        # Deleting field 'Puppies.mother_titles_ru'
        db.delete_column(u'puppies_puppies', 'mother_titles_ru')

        # Deleting field 'Puppies.mother_training_en'
        db.delete_column(u'puppies_puppies', 'mother_training_en')

        # Deleting field 'Puppies.mother_training_ru'
        db.delete_column(u'puppies_puppies', 'mother_training_ru')

        # Deleting field 'Puppies.father_titles_en'
        db.delete_column(u'puppies_puppies', 'father_titles_en')

        # Deleting field 'Puppies.father_titles_ru'
        db.delete_column(u'puppies_puppies', 'father_titles_ru')

        # Deleting field 'Puppies.father_training_en'
        db.delete_column(u'puppies_puppies', 'father_training_en')

        # Deleting field 'Puppies.father_training_ru'
        db.delete_column(u'puppies_puppies', 'father_training_ru')

        # Deleting field 'Puppies.amount_en'
        db.delete_column(u'puppies_puppies', 'amount_en')

        # Deleting field 'Puppies.amount_ru'
        db.delete_column(u'puppies_puppies', 'amount_ru')


    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'puppies.puppies': {
            'Meta': {'object_name': 'Puppies'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'amount_en': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'amount_ru': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'father_health': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'father_pedigree': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'father_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'father_titles': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'father_titles_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'father_titles_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'father_training': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'father_training_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'father_training_ru': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'litter': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mother_health': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'mother_pedigree': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_titles': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_titles_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mother_titles_ru': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mother_training': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mother_training_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mother_training_ru': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['puppies']