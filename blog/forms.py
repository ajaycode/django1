__author__ = 'Ajay'

from django import forms
from .models.models import Person
from django.utils.translation import ugettext_lazy as _

class PersonForm (forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')
        labels = {
            'first_name': _('First Name'),
        }
        help_texts = {
            'last_name': _('Provide your surname or family name. In case of women, please provide the maiden name, ie. surname before marriage.'),
        }
        error_messages = {
            'last_name': {
                'max_length':_("This person's name is too long."),
            },
        }
