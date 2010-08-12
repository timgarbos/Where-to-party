from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class main(models.Model):
    def __unicode__(self):
        return self.title
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    tagline = models.CharField(max_length=500)
    footer_about = models.TextField()
    login_text = models.TextField()
    intro = models.TextField()


#menu stuff here.. google it
