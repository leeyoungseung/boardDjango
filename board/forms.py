from django import forms
from .models import Board
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BoardForm(forms.ModelForm):
	class Meta:
		model = Board
		fields = ('b_writer',
				  'b_email',
				  'b_subject',
			      'b_passwd',
				  'b_read_count',
				  'b_content',
			      'b_ip',
				  'b_file_name',
				  'b_file_size')
		widgets = {
			'b_writer' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '작성자 명', 'autofocus':'autofocus','required':'required'}),
			'b_email' : forms.TextInput(attrs={'id':'inputEmail', 'class':'form-control', 'placeholder':'Email address', 'required':'required'}),
			'b_subject' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name', 'required':'required'}),
			'b_passwd' : forms.TextInput(attrs={'id':'inputPassword', 'class':'form-control', 'placeholder':'Password', 'required':'required'}),
			'b_content': forms.Textarea(attrs={'class':'form-control'}),
			'b_ip': forms.TextInput(attrs={'class': 'form-control'}),
			'b_file_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'File Name'})
		}


class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email", "username")

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None