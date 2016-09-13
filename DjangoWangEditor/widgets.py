#coding: utf-8

from django import forms  
from django.conf import settings  
from django.utils.safestring import mark_safe  
from django.template.loader import render_to_string  
from django.template import RequestContext  
from django.utils.translation import ugettext_lazy as _  

from django.contrib.admin.widgets import AdminTextareaWidget

class WangEditorWidget(forms.Textarea):  

    class Media:  
        css = {
              'all': ('/wangeditor/static/css/wangEditor.css',),  
        }

    def __init__(self, attrs = {}):
        #attrs['style'] = "width:800px;height:400px;visibility:hidden;"
        super(WangEditorWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WangEditorWidget, self).render(name, value, attrs)

        # 传入模板的参数
        editor_id = "id_%s" % name.replace("-", "_")
        uSettings = {
        	"name": name,
        	"id": editor_id,
        	"value": value
        }
        context = {
            'WEditor': uSettings,
        }
        return rendered  + mark_safe(render_to_string('wangeditor.html', context))

class AdminWEditorWidget(AdminTextareaWidget,WangEditorWidget):
    def __init__(self, **kwargs):
        super(AdminWEditorWidget, self).__init__(**kwargs)