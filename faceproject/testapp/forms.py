from django import forms
from testapp.models import face
class faceForm(forms.ModelForm):
    class Meta:
        model=face
        fields='__all__'