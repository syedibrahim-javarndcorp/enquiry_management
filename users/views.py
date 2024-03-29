from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import CustomUserForm, ProfileForm
from .models import Profile


# Create your views here.

def login_page(request):
    # To redirect user from seeing login page if they are already logged in
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('username/password incorrect')

    return render(request, 'users/login-register.html')


def logout_page(request):
    logout(request)
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('edit-account')

    context = {'page': page,
               'form': form,
               }
    return render(request, 'users/login-register.html', context)


def profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profile = Profile.objects.filter(name__icontains=search_query)
    context = {
        'profiles': profile,
        'search_query': search_query
    }
    return render(request, 'users/profiles.html', context)


@login_required(login_url='login')
def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}

    return render(request, 'users/user-profiles.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profiles')
    context = {'form': form}
    return render(request, 'users/profile-edit.html', context)
