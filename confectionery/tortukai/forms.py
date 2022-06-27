from django import forms
from django.conf import settings
from tinymce.widgets import TinyMCE
from .models import CakeReview


class CakeReviewForm(forms.ModelForm):
    class Meta:
        model = CakeReview
        fields = ('content', 'cake', 'client', )
        widgets = {
            'content': TinyMCE(mce_attrs=settings.TINYMCE_USER_CONFIG),
            'cake': forms.HiddenInput(),
            'client': forms.HiddenInput(),
        }
