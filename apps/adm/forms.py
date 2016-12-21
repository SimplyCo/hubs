# -*- coding: utf-8 -*-

from django import forms

from apps.hubsapp.models import Tag, Hub, Post


# from redactor.widgets import RedactorEditor


class AdminTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        # widgets = {
        #     'text': RedactorEditor(),
        #     'short_text': RedactorEditor(),
        # }


#####
class AdminHubForm(forms.ModelForm):
	class Meta:
		model = Hub
		fields = ['author', 'title', 'slug', 'description', 'image']


class AdminPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'slug', 'leading_image', 'short_text', 'full_text', 'status', 'placement', 'hub']
#####
