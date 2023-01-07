from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "home.html"


class SignUpPageView(generic.CreateView):
    template_name = "signup.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm
