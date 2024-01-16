# Use this if Function-based view
# from django.shortcuts import render

# # Create your views here.

from django.views.generic import TemplateView
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["my_thing"] = "Hello world this is from context handler" 

        context["posts"] = Post.objects.all()
        return context
