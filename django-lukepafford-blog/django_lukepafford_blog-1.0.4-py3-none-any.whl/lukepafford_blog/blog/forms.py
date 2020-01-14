from django import forms


class UploadPostForm(forms.Form):
    file = forms.FileField()
