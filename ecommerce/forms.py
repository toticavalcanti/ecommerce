from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attr={"class": "form-control", "id": "form_full_name"}))
    email     = forms.EmailField()
    content   = forms.CharField()