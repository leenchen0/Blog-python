from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from DjangoWangEditor.models import WangEditorField
# Create your models here.

class Article(models.Model):
    State_choices = {
        (0, u'Public'),
        (1, u'Draft'),
        (-1, u'Delete'),
    }

    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(choices=State_choices) #0 public,1 ,-1 delete.
    # content = UEditorField(u'content   ',width=1200, height=300, toolbars="full", imagePath="uploads/images/", filePath="uploads/files/", upload_settings={"imageMaxSize":1204000},
    #          command=None,blank=True)
    content = WangEditorField(u'content', width=1200, height=600, blank=True)
    def __unicode__(self):
        return self.title+"   "+str(self.article_id)

class Article_sort(models.Model):
    article_type = models.CharField(max_length=50);
    article_id = models.ForeignKey(Article);
    def __unicode__(self):
        return self.article_type

class Article_tag(models.Model):
    Tag_name = models.CharField(max_length=50);
    def __unicode__(self):
        return self.Tag_name

class TagToArt(models.Model):
    article_id = models.ForeignKey(Article);
    tag_id = models.ForeignKey(Article_tag);
    def __unicode__(self):
        return self.tag_id.Tag_name+u' To '+str(self.article_id.article_id)

class viewer(models.Model):
    article_id = models.CharField(max_length = 10);
    date = models.DateTimeField(auto_now_add=True);
    ip = models.CharField(max_length=30);
    isp = models.CharField(max_length=50);
    browser = models.CharField(max_length=30);
    os = models.CharField(max_length=30);
    def __unicode__(self):
        return str(self.date)+self.isp

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    Name = models.CharField(max_length=50, blank=True)
    HeadImg = models.CharField(max_length=300, blank=True)
    def __unicode__(self):
        return self.Name

class comment(models.Model):
    user = models.ForeignKey(User);
    article_id = models.CharField(max_length = 10, null=True);
    last_id = models.IntegerField(null=True);
    date = models.DateTimeField(auto_now_add=True, null=True);
    content = models.CharField(max_length=10000, null=True);
    user_ip = models.CharField(max_length=30, null=True);
    user_isp = models.CharField(max_length=50, null=True);
    user_browser = models.CharField(max_length=30, null=True);
    user_os = models.CharField(max_length=30, null=True);
    def __unicode__(self):
        return str(self.date) + str(self.user.userprofile.Name)