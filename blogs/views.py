from django.shortcuts import render, redirect
from .models import Blog, Post, House, City, Oblast
from .forms import CreateBlogForm, CreatePostForm


def home_page(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(owner_id=request.user.id).order_by('-created_at')
        return render(request, 'blogs/index.html', {'blogs': blogs})
    else:
        return redirect('/auth/login/')


def create_blog_page(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login/')

    if request.method == 'GET':
        form = CreateBlogForm()
        return render(request, 'blogs/create-blog.html', {'form': form})

    if request.method == 'POST':
        form = CreateBlogForm(request.POST)
        if not form.is_valid():
            return render(request, 'blogs/create-blog.html', {'form': form})

        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        city = form.cleaned_data['city']
        oblast = form.cleaned_data['oblast']
        house_address = request.POST.get('house_address')
        house = House.objects.get(name=house_address)

        blog = Blog(title=title, description=description, owner=request.user, house=house, city=city, oblast=oblast)
        blog.save()
        return redirect('/')


def blog_details_page(request, pk):
    if request.method == 'GET':
        form = CreatePostForm()
        blog = Blog.objects.get(id=pk)
        posts = Post.objects.filter(blog_id=pk)
        return render(request, 'blogs/blog-details.html', {'blog': blog, 'user': request.user, 'form': form,
                                                           'posts': posts})


def delete_blog_page(request, pk):
    if request.method == 'GET':
        blog_obj = Blog.objects.get(id=pk)
        if request.user.id == blog_obj.owner.id:
            blog_obj.delete()
            return redirect('/')
        return redirect('/')


def create_post(request, pk):
    if request.method == 'POST':
        blog_obj = Blog.objects.get(id=pk)
        if request.user.id == blog_obj.owner_id:
            form = CreatePostForm(request.POST)
            if form.is_valid():
                title = form.data.get('title')
                content = form.data.get('content')
                post = Post(title=title, content=content, blog_id=blog_obj.id)
                post.save()
                return redirect('/blogs/' + str(blog_obj.id) + '/')
            else:
                return render(request, 'blogs/blog-details.html', {'blog': blog_obj, 'user': request.user, 'form': form})
        else:
            return redirect('/')


def delete_post(request, pk):
    post_obj = Post.objects.get(id=pk)
    if post_obj.blog.owner.id == request.user.id:
        post_obj.delete()
        return redirect('/blogs/' + str(post_obj.blog.id) + '/')


def post_details(request, pk):
    post_obj = Post.objects.get(id=pk)
    return render(request, 'blogs/post-details.html', {'post': post_obj})
