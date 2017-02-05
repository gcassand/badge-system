from django import forms

from models import Model3d


class Model3dForm(forms.ModelForm):
    title = forms.TextInput()
    description = forms.Textarea()
    path = forms.FileField()

    class Meta:
        model = Model3d
        exclude = ["user", "views", "votes"]
