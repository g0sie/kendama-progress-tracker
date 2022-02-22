from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Row

from .models import Trick


class TrickForm(forms.ModelForm):
    class Meta:
        model = Trick
        fields = ['name', 'difficulty']
        widgets = {
            'difficulty': forms.RadioSelect(
                choices=(
                    ('b', 'beginner'),
                    ('i', 'intermediate'),
                    ('a', 'advanced'),
                    ('o', 'other')),
                attrs={'class': 'form-control'}
            )
        }
        labels = {
            'name': _('nazwa triku'),
            'difficulty': _('poziom trudności'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'add'
        self.helper.layout = Layout(
            Row('name', css_class='row mb-3'),
            Row('difficulty', css_class='row mb-3'),
            ButtonHolder(
                Submit('submit', 'dodaj', css_class='btn btn-secondary'),
                css_class='d-flex justify-content-start'
            ),
        )
