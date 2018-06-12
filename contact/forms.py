from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # website = forms.URLField(help_text=_('Website...'))
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
