# Django imports.
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Blog app imports
from blog.forms.dashboard.minister.minister_forms import (
    UserUpdateForm,
    ProfileUpdateForm,
)


class MinisterProfileView(LoginRequiredMixin, View):
    """
    Displays minister profile details
    """
    template_name = "dashboard/minister/minister_profile_detail.html"
    context_object = {}

    def get(self, request):
        minister = User.objects.get(username=request.user)

        self.context_object['minister_profile_details'] = minister
        return render(request, self.template_name, self.context_object)


class MinisterProfileUpdateView(LoginRequiredMixin, View):
    """
     Updates minister profile details
    """
    template_name = 'dashboard/minister/minister_profile_update.html'
    context_object = {}

    def get(self, request):
        user_form = UserUpdateForm(instance=self.request.user)
        profile_form = ProfileUpdateForm(instance=self.request.user.profile)

        self.context_object['user_form'] = user_form
        self.context_object['profile_form'] = profile_form

        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(data=request.POST, instance=self.request.user)
        profile_form = ProfileUpdateForm(data=request.POST, files=request.FILES,
                                         instance=self.request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            messages.success(request, f'Your account has successfully '
                                      f'been updated!')
            return redirect('blog:minister_profile_details')

        else:
            user_form = UserUpdateForm(instance=self.request.user)
            profile_form = ProfileUpdateForm(instance=self.request.user.profile)

            self.context_object['user_form'] = user_form
            self.context_object['profile_form'] = profile_form

            messages.error(request, f'Invalid data. Please provide valid data.')
            return render(request, self.template_name, self.context_object)



