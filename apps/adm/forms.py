# -*- coding: utf-8 -*-

from django import forms

from apps.hubsapp.models import Tag


# from redactor.widgets import RedactorEditor


class AdminTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        # widgets = {
        #     'text': RedactorEditor(),
        #     'short_text': RedactorEditor(),
        # }
