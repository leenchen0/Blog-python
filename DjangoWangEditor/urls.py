from django.conf.urls import url
from views import uploadFile

import os
from django.conf import settings
STATIC_ROOT = os.path.join(settings.STATIC_ROOT, 'editor')
MEDIA_ROOT = settings.MEDIA_ROOT

urlpatterns = [
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
	url(r'upload/', uploadFile),
]