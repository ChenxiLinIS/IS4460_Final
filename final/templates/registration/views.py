
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('kdrama_list')  # Redirect to kdrama_list.html upon successful login
        else:
            error_message = "Wrong username or password, please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html', {})
