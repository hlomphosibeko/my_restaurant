from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Menu, CustomerComment
from .forms import CustomerCommentForm


# Create your views here.
class MenuList(generic.ListView):
    queryset = Menu.objects.all()
    template_name = "menu/menu.html"


def menu_detail(request, slug):
    """
    Display an individual :model:`menu.Menu`.

    **Context**

    ``post``
        An instance of :model:`menu.Menu`.

    **Template:**

    :template:`menu/menu_detail.html`
    """
    queryset = Menu.objects.all()
    meal = get_object_or_404(queryset, slug=slug)
    customer_comments = meal.comments.all().order_by("-created_on")

    if request.method == "POST":
        customer_form = CustomerCommentForm(data=request.POST)
        if customer_form.is_valid():
            comment = customer_form.save(commit=False)
            comment.customer = request.user
            comment.meal = meal
            comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted!'
        )

    customer_form = CustomerCommentForm()

    return render(
        request,
        "menu/menu_detail.html",
        {
            "meal": meal,
            "customer_comments": customer_comments,
            "customer_form": customer_form,
        },
    )


def customer_comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Menu.objects.all()
        meal = get_object_or_404(queryset, slug=slug)
        customer_comments = get_object_or_404(CustomerComment, pk=comment_id)
        customer_form = CustomerCommentForm(
            data=request.POST, instance=customer_comments)

        if customer_form.is_valid() and customer_comments.customer == request.user:
            comment = customer_form.save(commit=False)
            comment.meal = meal
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))


def customer_comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = Menu.objects.all()
    meal = get_object_or_404(queryset, slug=slug)
    customer_comments = get_object_or_404(CustomerComment, pk=comment_id)

    if customer_comments.customer == request.user:
        customer_comments.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))


def order_details(request, slug, ):
    """
    view customer order
    """
    queryset = Menu.objects.all()
    