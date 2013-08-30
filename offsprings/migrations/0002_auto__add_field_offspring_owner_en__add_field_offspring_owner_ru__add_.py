# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Offspring.owner_en'
        db.add_column(u'offsprings_offspring', 'owner_en',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.owner_ru'
        db.add_column(u'offsprings_offspring', 'owner_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.city_en'
        db.add_column(u'offsprings_offspring', 'city_en',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.city_ru'
        db.add_column(u'offsprings_offspring', 'city_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.titles_en'
        db.add_column(u'offsprings_offspring', 'titles_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.titles_ru'
        db.add_column(u'offsprings_offspring', 'titles_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.training_en'
        db.add_column(u'offsprings_offspring', 'training_en',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.training_ru'
        db.add_column(u'offsprings_offspring', 'training_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.about_dog_en'
        db.add_column(u'offsprings_offspring', 'about_dog_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Offspring.about_dog_ru'
        db.add_column(u'offsprings_offspring', 'about_dog_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Offspring.owner_en'
        db.delete_column(u'offsprings_offspring', 'owner_en')

        # Deleting field 'Offspring.owner_ru'
        db.delete_column(u'offsprings_offspring', 'owner_ru')

        # Deleting field 'Offspring.city_en'
        db.delete_column(u'offsprings_offspring', 'city_en')

        # Deleting field 'Offspring.city_ru'
        db.delete_column(u'offsprings_offspring', 'city_ru')

        # Deleting field 'Offspring.titles_en'
        db.delete_column(u'offsprings_offspring', 'titles_en')

        # Deleting field 'Offspring.titles_ru'
        db.delete_column(u'offsprings_offspring', 'titles_ru')

        # Deleting field 'Offspring.training_en'
        db.delete_column(u'offsprings_offspring', 'training_en')

        # Deleting field 'Offspring.training_ru'
        db.delete_column(u'offsprings_offspring', 'training_ru')

        # Deleting field 'Offspring.about_dog_en'
        db.delete_column(u'offsprings_offspring', 'about_dog_en')

        # Deleting field 'Offspring.about_dog_ru'
        db.delete_column(u'offsprings_offspring', 'about_dog_ru')


    models = {
        u'dogs.gender': {
            'Meta': {'object_name': 'Gender'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'gender_en': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'gender_ru': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'offsprings.offspring': {
            'Meta': {'object_name': 'Offspring'},
            'about_dog': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'about_dog_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_dog_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'city_en': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'city_ru': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'dm': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'father': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']"}),
            'hd': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mdr1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'owner_en': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'owner_ru': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'pedigree': ('django.db.models.fields.URLField', [], {'max_length': '150', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sex': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dogs.Gender']"}),
            'titles': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'titles_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titles_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'training_en': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'training_ru': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['offsprings']