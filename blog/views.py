from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from blog.models import Post
from blog.serialazers import PostSerializer
from users.models import User


class BlogListView(generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/home.html'

    ordering = ['-publication_date']


def user_page(request):
    email = request.user.email
    posts = Post.objects.filter(user_email=email)
    user = User.objects.get(email=email)
    context = {"posts": posts, 'user': user}
    return render(request, 'blog/user_page.html', context)


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super(PostsViewSet, self).get_queryset()
        qs = qs.filter(user_email=self.request.user.email)
        return qs

    def perform_create(self, serializer):
        serializer.save(user_email=self.request.user.email)
