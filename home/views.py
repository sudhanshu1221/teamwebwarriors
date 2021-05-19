from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home_page(request):
    return render(request, 'home/home_page.html', {})


def handle_signup(request):
    if request.method == 'POST':
        email_add = request.POST['signEmail']

        user_name = request.POST['signUsername']
        type_pass = request.POST['signPassword']
        conf_pass = request.POST['cSignPassword']

        # Checks
        if len(user_name) > 10:
            messages.error(request, "Username can contain max 10 digits")
            return redirect('Home')
        if type_pass != conf_pass:
            messages.error(request, "Passwords are not matching")
            return redirect('Home')

        my_user = User.objects.create_user(user_name, email_add, type_pass)
        my_user.save()
        messages.success(request, "Your Account has been created successfully.")
        return redirect('Home')
    else:
        return HttpResponse("Not Allowed")


def handle_login(request):
    if request.method == 'POST':
        lin_user_name = request.POST['linUsername']
        lin_pass = request.POST['linPassword']

        user = authenticate(username=lin_user_name, password=lin_pass)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            print("Hello")
            return redirect('Home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('Home')

    return HttpResponse('404- Not Found')


def handle_logout(request):
    logout(request)
    messages.success(request, "Successfully logged in")
    return redirect('Home')
