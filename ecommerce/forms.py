from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Your full name"
                }
            )
        )
    email     = forms.EmailField()
    content   = forms.CharField()