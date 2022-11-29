from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from .form import SignupForm , UserForm , ProfileForm
from .models import Profile
# Create your views here.

def signup (request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate (username = username , password = password)
            login(request , user)
            return redirect ('accounts:login')
    else:
        form = SignupForm()
    context = {'form':form}
    return render (request , 'registration/signup.html' , context)

def profile(request):
    profile = Profile.objects.get(user = request.user) #get name of user from user
    context = {'profile' : profile}
    return render (request, 'accounts/profile.html' , context )


def editprofile(request):
    profile = Profile.objects.get(user = request.user) #get name of user from user
    
    if request.method == 'POST':
        userform = UserForm(request.POST , instance=request.user)
        profileform = ProfileForm(request.POST , request.FILES , instance=profile )
        if profileform.is_valid and userform.is_valid:
            userform.save()
            myprofileform = profileform.save(commit=False)
            myprofileform.user = request.user
            myprofileform.save()
            return redirect('accounts:profile')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    context = {'userform' : userform , 'profileform' : profileform}
    return render (request, 'accounts/profile_edit.html' , context )