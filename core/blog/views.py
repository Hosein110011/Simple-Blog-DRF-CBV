from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView,UpdateView, DeleteView
from .models import Post
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse




# def indexView(request):
    
#     context = {"name":"ali"}
#     return render(request, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["post"] = Post.objects.all()
        return context
        


class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'

    def get_redirect_url(self, *args: Any, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class ListView(PermissionRequiredMixin ,LoginRequiredMixin ,ListView):
    permission_required = "__all__"
    model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'
    # paginate_by = 2
    ordering = '-id'
    def get_queryset(self):
        posts = Post.objects.filter()
        return posts
    

class PostDetailView(LoginRequiredMixin ,DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# class PostCreateView(FormView):
#     template_name = 'contact.html'
#     form_class = PostForm
#     success_url = '/post/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    
    

class PostCreateView(PermissionRequiredMixin ,LoginRequiredMixin ,CreateView):
    model = Post
    permission_required = ''
    
    fields = ['title', 'content', 'status', 'category', 'published_date']
    success_url = '/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin ,UpdateView):
    model = Post
    fields = ['author','title', 'content', 'status', 'category', 'published_date']
    success_url = '/post/'


class PostDeleteView(LoginRequiredMixin ,DeleteView):
    model= Post
    success_url = '/post/'


