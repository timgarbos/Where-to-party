from django.db import models

class Place(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

class Post(models.Model):
    def __unicode__(self):
        return self.content
    pub_date = models.DateTimeField('date published')
    place = models.ForeignKey(Place)
    content = models.CharField(max_length=300)
