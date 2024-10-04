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
    if request.method == 'POST':
        user = User.objects.all().get(id=user_id)
        all_profiles = Profile.objects.all()
        result = []
        for a in all_profiles:
            if a.user.id == user_id:
                result.append(a)
        profile = result[0]
        name = request.POST.get('name')
        user.name = name
        user.save()
        bio = request.POST.get('bio')
        profile.bio = bio
        profile.save()
        return HttpResponse("Success!")


