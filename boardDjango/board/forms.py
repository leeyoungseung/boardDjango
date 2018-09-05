from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
	class Meta:
		model = Board
		fields = ('b_writer','b_email','b_subject',
			'b_passwd','b_read_count','b_content',
			'b_ip','b_file_name','b_file_size')
