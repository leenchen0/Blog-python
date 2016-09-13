from django import forms
from widgets import WangEditorWidget

class WangEditorModelForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(WangEditorModelForm, self).__init__(*args, **kwargs)