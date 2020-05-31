from django.shortcuts import render, redirect

# Create your views here.


from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/register.html"
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)