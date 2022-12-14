from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
# Ограничение доступа
from django.contrib.auth.mixins import LoginRequiredMixin

from ads.models import Post, Response


class IndexView(LoginRequiredMixin, TemplateView):
    """
    Ограничение доступа к странице с профилем (только для зарегистрированных).
    """
    template_name = 'profile/profile.html'


class UsersPostsView(ListView):
    """
    Все объявления пользователя.
    """
    model = Post
    template_name = 'profile/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-id']


class ResponsesForPostView(DetailView):
    """
    Все отклики на выбранное объявление.
    """
    model = Post
    template_name = 'profile/responses_for_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        obj = Post.objects.get(pk=id)
        # Для получения всех откликов на объявление.
        responses = Response.objects.filter(post=obj)
        context['responses'] = responses
        return context


def confirm_response(request, **kwargs):
    """
    Подтверждение отклика
    :param request:
    :param kwargs:
    :return:
    """
    pk = request.GET.get('pk', )
    response = Response.objects.get(pk=pk)
    post_id = response.post.pk
    response.confirmed = True
    response.save()
    return redirect(f'/profile/responses_for_post/{post_id}')
