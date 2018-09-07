from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    theme = forms.CharField(max_length=250)
    phone = forms.CharField()
    message = forms.TextInput()
