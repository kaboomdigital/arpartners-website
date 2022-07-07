from django import forms
from .models import Project
from django.forms import modelformset_factory


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'url', 'description', 'thumbnail', 'published', 'created_date', 'order_id', 'project_status')


ProjectFormSet = modelformset_factory(Project, fields=('name', 'url', 'description', 'thumbnail', 'published', 'created_date', 'order_id', 'project_status'))
