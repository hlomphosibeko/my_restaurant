from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Menu(models.Model):
    menu_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_menus'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category'
    )
    featured_image = models.ImageField('image', default='placeholder')
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.menu_title


class CustomerComment(models.Model):
    meal = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='comments'
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter'
    )
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=False)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.text} by {self.customer}"
