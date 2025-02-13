from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

from web.models import *
from django.contrib.auth.hashers import check_password

# Create your views here.
def user_access(function):
    def wrapper(request, *args, **kw):
        if 'login' not in request.session:
            return redirect('/login/')
        else:
            request.user = AdminUser.objects.get(id=request.session['id'])
            return function(request, *args, **kw)

    return wrapper

@user_access
def index(request):
    page_name = "Home"

    return render(request, 'index.html', {
        "page_name": page_name
    })


def login(request):
    if request.method == 'POST':
        data = request.POST
        try:
            user = AdminUser.objects.get(email=data['email'])
            if check_password(data['password'],user.password):
                request.session['login'] = True
                request.session['id'] = user.id
                return redirect('/')
            else:
                raise Exception("Incorrect")
        except:
            return render(request, 'login.html', {"error": "Check email/password combination"})
        
    return render(request, 'login.html')

def logout(request):
    request.session.clear()
    return redirect('/login/')



# Users Management

@user_access
def users(request):
    return render(request, 'users.html', {
        "page_name": "Users"
    })

@user_access
def users_show(request, user_id):
    return render(request, 'users-show.html', {
        "page_name": "Users"
    })

@user_access
def users_create(request):
    return render(request, 'users-create.html', {
        "page_name": "Users"
    })
    
    
    
# Settings Management
@user_access
def settings(request):
    return render(request, 'settings.html', {
        "page_name": "Settings"
    })