from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    comment = forms.CharField(required=True, label='', widget=forms.Textarea(attrs={'placeholder': 'Comment'}))
