from django import forms

class Word_Form(forms.Form):
    selection = forms.CharField(widget=forms.Textarea)
