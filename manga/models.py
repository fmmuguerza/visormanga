from django.db import models


class Manga(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')
    
class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name='chapters')
    chapter_title = models.CharField(max_length=200)
    chapter = models.IntegerField(default=0)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')
    
class Page(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='images')
    image = models.ImageField()
    page_number = models.IntegerField(default=0)
