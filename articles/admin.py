from django.contrib import admin
from .models import Article, Article_sort, Article_tag, TagToArt, comment

admin.site.register(Article),
admin.site.register(Article_sort),
admin.site.register(Article_tag),
admin.site.register(TagToArt),
admin.site.register(comment),
# Register your models here.
