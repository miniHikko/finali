from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewsForm, ComitForm
from .models import Post, Coment, User


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


class create_comit(LoginRequiredMixin, CreateView):
    form_class = ComitForm
    model = Coment
    template_name = 'comit.html'


@login_required
def Comittoouser(reguest):
    context = {'comit'}
    user = request.User
    userPost = user.objects.all(Post)
    usertopost = userPost.objects.all(Coment)
    return render(request=request, template_name='comituser.html', context=context)


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


class Comituser(LoginRequiredMixin, ListView):
    model = Coment
    ordering = '-id'
    template_name = 'comituser.html'
    context_object_name = 'comit'
    paginate_by = 10
