"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings

from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('home.urls')),
    url(r'^view/', views.view_info),
    url(r'^about/', views.MyAbout),
    url(r'^contact/', views.MyContact),
    url(r'^home/', views.reindex),
    url(r'^search/', views.Search),
    url(r'^resource/', include('home.urls')),
    url(r'^articles/', include('articles.urls')),

    # url(r'^ueditor/',include('DjangoUeditor.urls' )),

    url(r'^logout/', include('articles.urls')),

    #url(r'gobye/',include('gobye.urls')),

    #url(r'wechat/', include('weixin.urls')),

    url(r'^wangeditor/', include('DjangoWangEditor.urls')),
]

#serve media file when using developing server
if settings.DEBUG is False:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT,}),
        ]
