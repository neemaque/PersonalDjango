from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import User, Profile, Follow


def profile(request, user_id):
    user = User.objects.all().get(id=user_id)
    all_profiles = Profile.objects.all()
    result = []
    for a in all_profiles:
        if a.user.id == user_id:
            result.append(a)
    profile = result[0]

    followers = Follow.objects.filter(Following = user)
    template = loader.get_template('profile_template.html')
    context = {'profile': profile, 'followers': followers}
    return HttpResponse(template.render(context, request))


def edit_profile(request, user_id):
    user = User.objects.all().get(id=user_id)
    all_profiles = Profile.objects.all()
    result = []
    for a in all_profiles:
        if a.user.id == user_id:
            result.append(a)
    profile = result[0]
    if request.method == 'GET':
        template = loader.get_template('profile_edit_template.html')
        context = {'profile': profile}
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        name = request.POST.get('name')
        user.name = name
        user.save()
        bio = request.POST.get('bio')
        profile.bio = bio
        profile.save()
        return HttpResponse("Success!")


def follow_user(request, user_id):
    user = User.objects.all().get(id=user_id)
    if request.method == 'POST':
        follower_id = int(request.POST.get('follower_id'))
        follower = User.objects.all().get(id=follower_id)
        result = []
        for a in Follow.objects.all():
            if a.Follower == follower and a.Following == user:
                result.append(a)
        if len(result) != 0:
            return HttpResponse("Already follows!")
        follow = Follow(Follower = follower, Following = user)
        follow.save()
        return HttpResponse("Success!")


def unfollow_user(request, user_id):
    user = User.objects.all().get(id=user_id)
    if request.method == 'POST':
        follower_id = int(request.POST.get('follower_id'))
        follower = User.objects.all().get(id=follower_id)
        result = []
        for a in Follow.objects.all():
            if a.Follower == follower and a.Following == user:
                result.append(a)
        try:
            follow = result[0]
            follow.delete()
            return HttpResponse("Success!")
        except:
            return HttpResponse("User doesn't follow!")


def register(request):
    if request.method == 'GET':
        template = loader.get_template('register_template.html')
        context = {}
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        name = request.POST.get('name')
        user = User(name=name)
        user.save()
        bio = request.POST.get('bio')
        profile = Profile(user=user, bio=bio)
        profile.save()
        return HttpResponse("Success!")
