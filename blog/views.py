from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Blog,Comment
from .forms import BlogCreationForm, BlogUpdateForm, AddCommentForm
from django.contrib.auth.decorators import login_required


def index(request):
    """ Home page """ # Get the current page object
    return render(request, 'blog/index.html')

@login_required(login_url='accounts:login')
def detail(request, blog_id):
    """ Get a specific blog """
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog).order_by('published_date')
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user  # Assuming logged-in users are adding comments
            comment.save()
            return redirect('blog:detail', blog_id=blog_id)
    else:
        form = AddCommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)

@login_required(login_url='accounts:login')
def list(request):
    """ Home page """
    blogs = Blog.objects.all().order_by('-published_date')
    paginator = Paginator(blogs, 5)  # 5 blogs per page
    page_number = request.GET.get('page')  # Get the current page number from the URL query
    page_obj = paginator.get_page(page_number)  # Get the current page object
    return render(request, 'blog/list.html', {'page_obj': page_obj})

@login_required(login_url='accounts:login')
def user_blog(request):
    """ Get the user's blogs """
    blogs = Blog.objects.filter(author=request.user).order_by('-published_date')
    return render(request, 'blog/user_blog.html', {'blogs': blogs})
    
    
    

@login_required(login_url='accounts:login')
def create(request):
    """ Create a new blog """
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            blog = Blog.objects.create(
                author=request.user,
                title=data['title'],
                text=data['text'],
            )
            if blog:
                blog.save()
                messages.success(request, "Blog created successfully.")
                return redirect('blog:list')
            
            else:
                messages.error(request, "There is an error.", 'danger')
                
        return render(request, 'blog/create.html', {'form':form})
    
    else:
        form = BlogCreationForm
        return render(request, 'blog/create.html', {'form':form})

@login_required(login_url='accounts:login')
def update(request, blog_id):
    """ Modify the blog """
    blog = get_object_or_404(Blog,pk=blog_id)
    if request.user != blog.author:
        messages.error(request, "You don't have permission to delete this blog.", 'danger')
        return redirect('blog:index')
    
    if request.method == 'POST':
        form = BlogUpdateForm(request.POST, instance=blog)
        if form.is_valid():
            data = form.cleaned_data
            if blog.author == request.user:
                 blog.title = data['title']
                 blog.text = data['text']
                 blog.save()
                 messages.success(request, f'{blog.title} updated successfully. ')
                 return redirect('blog:list')
             
            else:
                messages.error(request, 'You are not allowed do edit this blog. ', 'danger')
                
        return render(request, 'blog/update.html', {'form':form})
    
    else:
        form = BlogUpdateForm(instance=blog)
        return render(request, 'blog/update.html', {'form':form})

@login_required(login_url='accounts:login')
def delete(request, blog_id):
    """ Delete the blog """
    blog = get_object_or_404(Blog,pk=blog_id)
    if request.user == blog.author:
        if request.method == "POST":
            blog.delete()
            return redirect('blog:list')
        
        else:
            return render(request, "blog/delete.html", {'blog':blog})
    
    else:
        messages.error(request, "You don't have permission to delete this blog.", 'danger')
        return redirect('blog:index')