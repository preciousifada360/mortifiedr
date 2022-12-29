# Django imports.
from contextlib import redirect_stderr
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import  PermissionRequiredMixin, AccessMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required

# Blog app imports
from blog.forms.account.login_forms import UserLoginForm

class UserAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect ('/')
        if not self.has_permission():
            return redirect ('/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class UserLoginView(View):
            
    """
     Logs minister into dashboard.
    """
    template_name = 'account/login.html'
    context_object = {"login_form": UserLoginForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        login_form = UserLoginForm(data=request.POST)

        if login_form.is_valid():
            
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            
            if user:
                login(request, user)
                messages.success(request, f"Login Successful ! "
                                          f"Welcome {user.username}.")
                if not self.request.user.is_staff:
                    return redirect ('/')
                if self.request.user.is_staff:
                    return redirect('blog:dashboard_home')

            else:
                messages.error(request,
                               f"Invalid Login details: {username}, {password} "
                               f"are not valid username and password !!! Please "
                               f"enter a valid username and password.")
                return render(request, self.template_name, self.context_object)

        else:
            messages.error(request, f"Invalid username and password")
            return render(request, self.template_name, self.context_object)




