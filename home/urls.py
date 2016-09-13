from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^view/',views.view_info),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/home/pencil/MyBlog/mysite/home/templates/static'}),
]
