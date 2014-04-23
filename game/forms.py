import os
from django import forms
from models import Teacher
from django import forms

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['avatar']

class AvatarPreUploadedForm(forms.Form):
	def __init__(self, *args, **kwargs):
		choices = kwargs.pop('my_choices')
		super(AvatarPreUploadedForm, self).__init__(*args, **kwargs)
	 	self.fields['avatars'] = forms.ChoiceField(choices=choices)

	class Meta:
		model = Teacher
		fields = ('avatar',)