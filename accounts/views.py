from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


def signin(request):
        if request.method == "POST":
            email = request.POST['email']
            pass1 = request.POST['pass1']

            user = authenticate(email=email, password=pass1)

            if user is not None:
                login(request, user)
                fname= user.first_name
                return render(request,"authentication/index.html",{'fname':fname})

            else:
                messages.error(request, "Incorrect Credentials")
                return redirect('home')
        return render(request,"authentication/signin.html")




		


def signup(request):
        if request.method == "POST":
            # username =request.POST.get('username')
            username =request.POST['username']
            fname =request.POST['fname']
            lname =request.POST['lname']
            email =request.POST['email']
            pass1 =request.POST['pass1']
            pass2 =request.POST['pass2']


            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            

            messages.success(request, "Your Acc has been successfully created.")

            return redirect('login')
        return render(request,"accounts/register.html")























		