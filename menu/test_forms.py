from django.test import TestCase
from .forms import CustomerCommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        customer_form = CustomerCommentForm({'text': 'This is a great meal'})
        self.assertTrue(customer_form.is_valid())

    def test_form_is_invalid(self):
        customer_form = CustomerCommentForm({'text': ''})
        self.assertFalse(customer_form.is_valid(), msg="Form is valid")
