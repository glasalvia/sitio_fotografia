# send_email/forms.py
from django import forms


class ContactForm(forms.Form):
    Email = forms.EmailField(required=True)
    Asunto = forms.CharField(required=True)
    Mensaje = forms.CharField(widget=forms.Textarea, required=True)