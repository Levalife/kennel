# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from news.models import News
from dogs.models import Dog, Gender
from offsprings.models import Offspring
from puppies.models import Puppies
from gallery.models import Image, Album



class NewsTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Modelka.
    """
    
    fields = ('title', 'body',)

class GenderTranslationOptions(TranslationOptions):
    fields = ('gender', )

class DogTranslationOptions(TranslationOptions):
    fields = ('breeder', 'titles', 'training', 'about_dog')

class OffspringTranslationOptions(TranslationOptions):
    fields = ('owner', 'city', 'titles', 'training', 'about_dog')

class PuppiesTranslationOptions(TranslationOptions):
    fields = ('mother_titles', 'mother_training', 'father_titles', 'father_training', 'amount')

class AlbumTranslationOptions(TranslationOptions):
    fields = ('title', )

class ImageTranslationOptions(TranslationOptions):
    fields = ('title', )

translator.register(News, NewsTranslationOptions)
translator.register(Gender, GenderTranslationOptions)
translator.register(Dog, DogTranslationOptions)
translator.register(Puppies, PuppiesTranslationOptions)
translator.register(Offspring, OffspringTranslationOptions)
translator.register(Album, AlbumTranslationOptions)
translator.register(Image, ImageTranslationOptions)