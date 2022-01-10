from django.forms import ModelForm
from .models import Ems


class EmsForm(ModelForm):
    class Meta:
        model = Ems
        fields = ['name', 'title', 'description', 'tag']
