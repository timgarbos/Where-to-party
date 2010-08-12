from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Place(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    owners = models.ManyToManyField(User)
    description = models.TextField()
    paidFrom = models.DateField()
    paidTo = models.DateField()
    image = models.ImageField(upload_to='places', null=True, blank=True)
    profileImage = models.ImageField(upload_to='places', null=True, blank=True)

class Post(models.Model):
    def __unicode__(self):
        return self.content
    pub_date = models.DateTimeField('date published')
    place = models.ForeignKey(Place)
    content = models.TextField()
   # author = models.ForeignKey(User)


from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
