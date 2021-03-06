from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from .models import Post
from .forms import PostForm

# try adding generic.ListView to this and def_getqueryset
def post_list(request) :
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = posts[::-1]
	post_count = Post.objects.count()
	date = datetime.now()
	return render(request, 'blog/post_list.html', {'posts': posts, 'date': date, 'post_count': post_count})

def post_detail(request, pk) :
	post = get_object_or_404(Post, pk=pk)
	date = datetime.now()
	return render(request, 'blog/post_detail.html', {'post': post, 'date': date})

def post_new(request) :
	# form = PostForm()
	# date = datetime.now()
	# return render(request, 'blog/post_edit.html', {'form': form, 'date': date})

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
		    post = form.save(commit=False)
		    post.author = request.user
		    post.published_date = timezone.now()
		    post.save()
		    return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def cv(request) :
	date = datetime.now()
	return render(request, 'blog/cv.html', { 'date': date})

