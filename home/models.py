from __future__ import unicode_literals

from django.db import models

class viewer(models.Model):
    date = models.DateTimeField(auto_now_add=True);
    ip = models.CharField(max_length=30);
    isp = models.CharField(max_length=50);
    browser = models.CharField(max_length=30);
    os = models.CharField(max_length=30);
    def __unicode__(self):
        return str(self.date)+self.isp
# Create your models here.
