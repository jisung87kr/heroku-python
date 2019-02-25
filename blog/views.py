import math

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
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
    return render(request, 'blog/post.html', {'post': post})

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.title = request.POST['title']
            post.author = request.user
            post.content = request.POST['content']
            post.created_date = request.POST['created_date']
            post.published_date = request.POST['published_date']
            post.save()
            return HttpResponseRedirect(reverse('blog:post', args=(post.pk,)))
    else :
        form = PostForm()
        return render(request, 'blog/write.html', {'form': form})
