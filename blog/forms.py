from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	"""For sending the content on form in models"""
	
	class Meta:
		model = Post
		fields = ('title', 'text',)
		