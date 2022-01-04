"""Users views."""

# Django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import (reverse, reverse_lazy)
from django.views.generic import (DetailView, FormView, UpdateView)
from posts.models import Post

# Locals
from users.forms import (SignupForm)
from users.models import (Profile, User)


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_ulr = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'


class UpdateProfileView(LoginRequiredMixin, UpdateView):

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class UserDatailView(LoginRequiredMixin, DetailView):

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
