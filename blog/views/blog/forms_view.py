# Core Django imports.
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (

    ListView,
)


# Blog application imports.
from blog.models.form_models import Form


class FormsListView(ListView):
    model = Form
    fields = ["name", "image", "form_url"]
    paginate_by = 12
    context_object_name = 'forms'
    template_name = 'blog/form_list.html'

    def get_queryset(self):
        return Form.objects.order_by('-date_created')