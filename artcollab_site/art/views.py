from venv import create
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request
from .forms import SignupForm, HomeForm
from .models import Contact, Skillset, UserProfile

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.password = make_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.save()
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            bio = form.cleaned_data['bio']
            profile = user.userprofile_set.create(gender=gender,age=age,bio=bio)
            skill = form.cleaned_data['skill_set']
            for i in skill:
                s = Skillset.objects.get(skill=i)
                s.save()
                profile.skill_set.add(s)
            profile.save()
            facebook_link = form.cleaned_data['fb_link']
            instagram_link = form.cleaned_data['instagram_link']
            youtube_link = form.cleaned_data['youtube_link']
            other_sites = form.cleaned_data['other_link']
            phone = form.cleaned_data['phone number']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            city =  form.cleaned_data['city']
            contact = user.contact_set.create(facebook_link=facebook_link, instagram_link=instagram_link,youtube_link=youtube_link, other_sites=other_sites, phone=phone, country=country, state=state, city=city)
            contact.save()
            return redirect('/art/login/')
        else:
            return HttpResponse('invalid form: plesse check the details filled')
    else:
        """skill_list = Skillset.objects.all()"""
        form = SignupForm()
    return render(request, 'registration/signup.html',{'form': form})


def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            global username
            username = form.cleaned_data['username']
            global skill_set
            skill_set = form.cleaned_data['skill_set']
            global country_name
            country_name = form.cleaned_data['country']
            global state_name
            state_name = form.cleaned_data['state']
            global city_name
            city_name = form.cleaned_data['city']
            return redirect('/art/collab')
        else:
            return HttpResponse('invalid input')
    else:
        form=HomeForm()
    return render(request, 'home.html',{'form': form})

def collab(request):
    return render(request,'collab.html',{})