#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

# get settings
from settings import UploadSettings
# get a unique id by uuid.uuid4()
import uuid


def save_upload_file(PostFile,FilePath):
	'''
		save upload file
	'''
	try:
		f = open(FilePath, 'wb')
		for chunk in PostFile.chunks():
			f.write(chunk)
	except Exception,E:
		f.close()
		return u"writing file error:"+ E.message
	f.close()
	return u"SUCCESS"

@csrf_exempt
def uploadFile(req):
	'''
		handle upload files
	'''
	# check method's type
	if req.method != "POST":
		return HttpResponse("error|request.method!=post")

	# get the upload file
	file = req.FILES.get('upload_file', None)
	if file is None:
		return HttpResponse("error|get file error")

	upload_file_name = file.name
	upload_file_size = file.size

	# get upload original name and file's extension
	upload_original_name,upload_original_ext=os.path.splitext(upload_file_name)

	# check file's type
	ALLOW_FILES_TYPE = UploadSettings['ALLOW_FILES_TYPE']
	if not upload_original_ext.lower() in ALLOW_FILES_TYPE:
		return HttpResponse("error|file type error")

	# get ouput_file_path
	OUTPUT_PATH = UploadSettings['OUTPUT_PATH']
	output_file_path, output_file_name = get_output_file_path(OUTPUT_PATH, upload_original_ext)

	# write file
	state = save_upload_file(file, output_file_path)

	if state != "SUCCESS":
		return HttpResponse("error|" + state)

	# cal file url
	EXTRA_PATH = UploadSettings["EXTRA_PATH"]
	file_url = os.path.join("/wangeditor/media", EXTRA_PATH, output_file_name)
	return HttpResponse(file_url)

def get_output_file_path(output_path, extension):
	'''
		get output file name by uuid.uuid4()
		find a unuserd filename

		return:
			the final file path
	'''
	uuid_str = uuid.uuid4().urn[9:]
	output_file_name = uuid_str + extension
	output_file_path = os.path.join(output_path, output_file_name)
	# if dir is not exist then create
	if not os.path.exists(output_path):
		os.makedirs(output_path)

	# find a unused filename
	while os.path.exists(output_file_path):
		output_file_name = uuid_str + extension
		output_file_path = os.path.join(output_path, output_file_name)

	return (output_file_path, output_file_name)