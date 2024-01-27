from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                'demo_link', 'source_link', 'tags']
        # adding class for styling in forms
        widgets = {
            'tags':forms.CheckboxSelectMultiple(), 
        }
    #another way of adding class for styling in forms
    def __init__(self,*args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # this works but repetitive
        # self.fields['title'].widget.attrs.update({'class': 'input', "placeholder": 'Add title',etc})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})