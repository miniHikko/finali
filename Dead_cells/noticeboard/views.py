from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .filters import NewsFilter
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

    def post(self, request, *args, **kwargs):
        appointment = Coment(
            coment_text=request.POST['coment_text'],
            user_coment_id=request.POST['user_coment'],
            post_coment_id=request.POST['post_coment'],
        )
        appointment.save()
        user = User.objects.get(id=request.POST['user_coment'])
        comcom = user.email

        # получаем наш html
        html_content = render_to_string(
            'comcrea.html',
            {
                'com': appointment,
            }
        )

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по-другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=appointment.post_coment,
            body=appointment.coment_text,  # это то же, что и message
            from_email='mrmolocko@yandex.ru',
            to=[comcom],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()  # отсылаем

        return HttpResponseRedirect('/noticeboard/')


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

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comit'] = Coment.objects.filter(post_coment__post_Author=self.request.user)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def prinit(self, request):
        self.model.status = True
        self.model.save()
        user = User.objects.get(id=request.POST['user_coment'])
        comcom = user.email

        # получаем наш html
        html_content = render_to_string(
            'comc.html',
            {
                'com': Coment,
            }
        )

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по-другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=Coment.post_coment,
            body=Coment.coment_text,  # это то же, что и message
            from_email='mrmolocko@yandex.ru',
            to=[comcom],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()  # отсылаем


class ComDelete(LoginRequiredMixin, DeleteView):
    model = Coment
    template_name = 'com_delete.html'
    context_object_name = 'comit'
    success_url = reverse_lazy('urcomit')
