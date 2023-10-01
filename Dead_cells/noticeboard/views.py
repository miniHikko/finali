from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewsForm
from .models import Post


class NoticeList(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-id'
    template_name = 'notice.html'
    context_object_name = 'notice'
    paginate_by = 10


class create_post(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = '/noticeboard/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.position = self.request.path
        return HttpResponseRedirect('/noticeboard/'), super().form_valid(form),



# def create_pos(reguest):
# form = NewsForm
# if reguest.method == "POST":
# form = NewsForm(reguest.POST)
# if form.is_valid():
# form.save()
# return render(reguest, 'news_edit.html', {"form": form}), HttpResponseRedirect('/noticeboard/')


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
