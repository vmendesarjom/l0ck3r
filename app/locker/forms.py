from django import forms

from .models import Projector

# User: create
class ProjectorForm(forms.ModelForm):

    def save(self, commit=True):
        projector = super(ProjectorForm, self).save(commit=False)
        if commit:
            projector.save()
        return projector

    class Meta:

        model = Projector