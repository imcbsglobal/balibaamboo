
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField(label="Your email")
    phone = forms.CharField(max_length=15, label="Phone Number")
    message = forms.CharField(widget=forms.Textarea, required=False, label="Your message (optional)")

