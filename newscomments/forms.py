from typing import Text
from django import forms
from django.forms.widgets import Textarea
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CommentForm(forms.Form):
    new_name = forms.CharField(required=True, max_length=20, help_text="ID")
    new_content = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    def clean_comment_form(self):
        data_name = self.cleaned_data['new_name']
        data_content = self.cleaned_data['new_content']

        if data_name == "" :
            raise ValidationError(_('Invalid name'))
        if data_content == "":
            raise ValidationError(_('Invalid content'))

        return data_name, data_content