from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CustomerCommentForm
from .models import Menu


class TestMenuViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="Lee",
            password="getameal2!"
        )
        self.menu = Menu(menu_title="Menu title", customer=self.user,
                         slug="menu-title", description="Menu description",
                         price=1)
        self.menu.save()

    def test_render_menu_detail_page_with_customer_form(self):
        response = self.client.get(reverse(
            'menu_detail', args=['menu-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Menu title", response.content)
        self.assertIn(b"Menu description", response.content)
        self.assertIsInstance(
            response.context['customer_form'], CustomerCommentForm)
