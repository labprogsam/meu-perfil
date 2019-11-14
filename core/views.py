from django.shortcuts import render
from django.views import generic
from .models import Series

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'myProfile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series"] = Series.objects.all()
        return context
        
