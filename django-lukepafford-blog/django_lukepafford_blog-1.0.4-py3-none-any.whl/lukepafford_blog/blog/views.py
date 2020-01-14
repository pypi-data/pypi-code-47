from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Posts
from .forms import UploadPostForm
from .markdown_parser import parse_yaml_post

# Create your views here.
class HomeView(TemplateView):
    template_name = "_base.html"


class PostList(ListView):
    model = Posts
    context_object_name = "posts"
    paginate_by = 10


class PostDetail(DetailView):
    model = Posts
    context_object_name = "post"


class PostUpload(LoginRequiredMixin, DetailView):
    def get(self, request):
        form = UploadPostForm
        return render(request, "blog/post_upload.html", {"form": form})

    def post(self, request):
        form = UploadPostForm(request.POST, request.FILES)
        if form.is_valid():
            parsed_data = parse_yaml_post(form.cleaned_data["file"])

            # Overwrite existing post if title is the same
            try:
                post = Posts.objects.get(title=parsed_data["title"])
            except Posts.DoesNotExist:
                post = Posts()

            post.title = parsed_data["title"]
            post.body = parsed_data["body"]
            post.author = request.user
            post.save()
        return redirect("posts_list")
