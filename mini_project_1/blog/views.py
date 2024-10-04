from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Post, Comment
from users.models import User

def post_list(request):
    #if request.method == "GET":
    posts = Post.objects.all()
    template = loader.get_template('posts_template.html')
    context = {'posts' : posts,}
    return HttpResponse(template.render(context, request))

def post(request, post_id):
    post = Post.objects.all().get(id=post_id)
    all_comments = Comment.objects.all()
    result = []
    for a in all_comments:
        if a.post.id == post_id:
            result.append(a)
    comments = result
    template = loader.get_template('post_template.html')
    context = {'post' : post, 'comments' : comments,}
    return HttpResponse(template.render(context, request))

    #if request.method == 'GET':

def create_post(request):
    template = loader.get_template('post_form_template.html')
    context = {}
    if request.method == 'GET':
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_id = int(request.POST.get('user_id'))
        user = User.objects.all().get(id=user_id)
        post = Post(title = title, content = content, author = user)
        post.save()
        return HttpResponse("Success!")

def edit_post(request, post_id):
    template = loader.get_template('post_edit_template.html')
    post = Post.objects.all().get(id=post_id)
    context = {'post': post}
    if request.method == 'GET':
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        return HttpResponse("Success!")

def delete_post(request, post_id):
    post = Post.objects.all().get(id=post_id)
    post.delete()
    return HttpResponse("Success!")

def comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.all().get(id=post_id)
        content = request.POST.get('content')
        user_id = int(request.POST.get('user_id'))
        user = User.objects.all().get(id=user_id)
        comment = Comment(content = content, post = post, author = user)
        comment.save()
        return HttpResponse("Success!")
