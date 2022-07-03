from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from authentication.forms import CreateUserForm, UserPermissionsForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from authentication.models import UserPermission
# Create your views here.

@login_required(login_url='login')
def registerUser(request):
    form = CreateUserForm()
    permissions_form = UserPermissionsForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        permissions_form = UserPermissionsForm(request.POST)

        if form.is_valid() and permissions_form.is_valid():
            user = form.save()
            permissions = permissions_form.save(commit=False)
            permissions.user = user
            permissions.save()

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created successfully for ' + username)
            return redirect('dashboard')

    context = {'form': form, 'permissions_form': permissions_form}
    return render(request, 'register.html', context)

@never_cache
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = AuthenticationForm()

        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.info(request, "Username or Password is incorrect")
            
        context = {'form': form}
        return render(request, 'login.html', context)


@never_cache
@login_required(login_url='login')
def dashboard(request):
    all_users = User.objects.all()
    context = {'all_users': all_users}
    return render(request, 'dashboard.html', context)


def logoutUser(request):
    logout(request)
    return render(request, 'logout.html')


@login_required(login_url='login')
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    form = CreateUserForm(instance=user)

    user_permissions = UserPermission.objects.get(user_id=pk)
    permissions_form = UserPermissionsForm(instance=user_permissions)

    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        permissions_form = UserPermissionsForm(request.POST, instance=user_permissions)

        if form.is_valid() and permissions_form.is_valid():
            user = form.save()
            permissions = permissions_form.save(commit=False)
            permissions.user = user
            permissions.save()
            return redirect('dashboard')

    context = {'form': form, 'permissions_form': permissions_form}
    return render(request, 'update.html', context)


@login_required(login_url='login')
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('dashboard')
    context = {'user': user}
    return render(request, 'delete.html', context)