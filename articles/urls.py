from django.conf.urls import url

from articles import views
from DjangoUeditor import urls as DjangoUeditor_urls
urlpatterns = [
    url(r'^$', views.Logout),
    url(r'^(?P<article_id>[0-9]+)/$', views.Detail),
    url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment_create),
    url(r'search/', views.Search),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/home/pencil/MyBlog/mysite/articles/templates/static'}),
]