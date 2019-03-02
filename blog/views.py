import math

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    if request.GET.get('q'):
            variable_column = request.GET.get('fd_name')
            search_type = 'contains'
            filter = variable_column + '__' + search_type
            posts = Post.objects.filter(**{ filter: request.GET.get('q') }, published_date__lte = timezone.now()).order_by('-published_date')
    else :
        posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 10)
    if request.GET.get('page'):
        page = request.GET.get('page')
    else :
        page = 1
    contacts = paginator.get_page(page)
    page_range = 5
    current_block = math.ceil(int(page)/page_range)
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]
    return render(request, 'blog/index.html', {
        'contacts': contacts,
        'p_range' : p_range,
    })

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    prevPost = Post.objects.filter(published_date__lte = timezone.now(), published_date__gt=post.published_date).order_by('published_date').first()
    nextPost = Post.objects.filter(published_date__lte = timezone.now(), published_date__lt=post.published_date).order_by('-published_date').first()
    return render(request, 'blog/post.html', {
        'post': post,
        'prevPost' : prevPost,
        'nextPost' : nextPost,
        })

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('blog:post', args=(post.pk,)))
    else :
        form = PostForm()
        return render(request, 'blog/write.html', {'form': form})

def modi(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('blog:post', args=(post.pk,)))
    else :
        form = PostForm(instance=post)
    return render(request, 'blog/write.html', {'form': form})
