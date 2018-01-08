from django import forms
from .models import Bills

class ChangeSignupForm(forms.Form):
	new_url = forms.CharField(
	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"enter only last part of url without space"}),
	max_length=75,
	required=False,
	label="New sign-up URL")
	def clean(self):
		cleaned_data = super(ChangeSignupForm, self).clean()
		if self.cleaned_data["new_url"]=="":
			self._errors['new_url'] = self.error_class([
					'Invalid url'])
			return cleaned_data
	class Meta:
		fields = ['new_url']


class ChangeMenuForm(forms.Form):
	new_url = forms.CharField(
	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"url"}),
	max_length=10000,
	required=False,
	label="URL of menu image")
	def clean(self):
		cleaned_data = super(ChangeMenuForm, self).clean()
		if self.cleaned_data["new_url"]=="":
			self._errors['new_url'] = self.error_class([
					'Invalid url'])
			return cleaned_data
	class Meta:
		fields = ['new_url']

class EditBillForm(forms.ModelForm):

	def clean(self):
		cleaned_data = super(EditBillForm, self).clean()
		return cleaned_data


	class Meta:
		model=Bills
		fields = ['month','bill']



