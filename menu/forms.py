from .models import CustomerComment
from django import forms


class CustomerCommentForm(forms.ModelForm):
    class Meta:
        model = CustomerComment
        fields = ('text',)
