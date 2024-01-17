# Use this if Function-based view
# from django.shortcuts import render

# # Create your views here.

from django.views.generic import TemplateView, DetailView, FormView
# ccbv.co.uk for django views documentation

from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):

    # you can access the model via {{ post }} keyword...
    template_name = "home.html"

    # setting context / View content
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["my_thing"] = "Hello world this is from context handler" 

        context["posts"] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):

    # you can access the model via {{ object }} keyword...
    # model = instance of a Post...
    template_name = "detail.html"
    model = Post 

class AddPostView(FormView):
    
    # you can access the form via {{ form }} keyword...
    template_name = "new_post.html"
    form_class = PostForm # imported from forms.py contains fields in form
    success_url = "/"
    
    def form_valid(self, form):
        
        # Data from form is saved here. note that dictionary is mapped 
        # via the defined values in forms.py
            # form.cleaned_data['text']
            # form.cleaned_data['image']
        
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        
        return super().form_valid(form)
    