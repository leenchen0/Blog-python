#coding: utf-8
from django.db import models
from django.contrib.admin import widgets as admin_widgets
from widgets import WangEditorWidget, AdminWEditorWidget


class WangEditorField(models.TextField):

	def __init__(self ,verbose_name=None, width=600, height=300, config={} ,**kwargs):
		self.weditor_settings = locals().copy()
		kwargs["verbose_name"] = verbose_name
		del self.weditor_settings["self"],self.weditor_settings["kwargs"],self.weditor_settings["verbose_name"]
		super(WangEditorField, self).__init__(**kwargs)

	def formfield(self, **kwargs):
		defaults = {'widget': WangEditorWidget(attrs=self.weditor_settings)}
		defaults.update(kwargs)
		if defaults['widget'] == admin_widgets.AdminTextareaWidget:
			defaults['widget'] = AdminWEditorWidget(attrs=self.weditor_settings)

		return super(WangEditorField, self).formfield(**defaults)
