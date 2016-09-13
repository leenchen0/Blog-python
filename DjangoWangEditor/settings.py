#coding: utf-8
# global settings
from django.conf import settings
import os

# upload settings
EXTRA_PATH = "upload"
UploadSettings = {
	"ALLOW_FILES_TYPE": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
	"EXTRA_PATH": "upload",
	"OUTPUT_PATH": os.path.join(settings.MEDIA_ROOT, EXTRA_PATH)
}