# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Gender.gender_en'
        db.add_column(u'dogs_gender', 'gender_en',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gender.gender_ru'
        db.add_column(u'dogs_gender', 'gender_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.breeder_en'
        db.add_column(u'dogs_dog', 'breeder_en',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.breeder_ru'
        db.add_column(u'dogs_dog', 'breeder_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.titles_en'
        db.add_column(u'dogs_dog', 'titles_en',
                      self.gf('django.db.models.fields.TextField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.titles_ru'
        db.add_column(u'dogs_dog', 'titles_ru',
                      self.gf('django.db.models.fields.TextField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.training_en'
        db.add_column(u'dogs_dog', 'training_en',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.training_ru'
        db.add_column(u'dogs_dog', 'training_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.about_dog_en'
        db.add_column(u'dogs_dog', 'about_dog_en',
                      self.gf('django.db.models.fields.TextField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dog.about_dog_ru'
        db.add_column(u'dogs_dog', 'about_dog_ru',
                      self.gf('django.db.models.fields.TextField')(max_length=400, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Gender.gender_en'
        db.delete_column(u'dogs_gender', 'gender_en')

        # Deleting field 'Gender.gender_ru'
        db.delete_column(u'dogs_gender', 'gender_ru')

        # Deleting field 'Dog.breeder_en'
        db.delete_column(u'dogs_dog', 'breeder_en')

        # Deleting field 'Dog.breeder_ru'
        db.delete_column(u'dogs_dog', 'breeder_ru')

        # Deleting field 'Dog.titles_en'
        db.delete_column(u'dogs_dog', 'titles_en')

        # Deleting field 'Dog.titles_ru'
        db.delete_column(u'dogs_dog', 'titles_ru')

        # Deleting field 'Dog.training_en'
        db.delete_column(u'dogs_dog', 'training_en')

        # Deleting field 'Dog.training_ru'
        db.delete_column(u'dogs_dog', 'training_ru')

        # Deleting field 'Dog.about_dog_en'
        db.delete_column(u'dogs_dog', 'about_dog_en')

        # Deleting field 'Dog.about_dog_ru'
        db.delete_column(u'dogs_dog', 'about_dog_ru')


    models = {
        u'dogs.dog': {
            'Meta': {'object_name': 'Dog'},
            'about_dog': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'about_dog_en': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'about_dog_ru': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'breeder': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'breeder_en': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'breeder_ru': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
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
            'titles_en': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'titles_ru': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'training_en': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'training_ru': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['dogs']