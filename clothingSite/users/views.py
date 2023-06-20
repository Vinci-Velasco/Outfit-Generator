from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, "users/index.html")

def signup_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "users/signup.html", {
                "message": "Username already exists!"
            })

        User.objects.create_user(username=username, password=password, email=email)

        # rendered login page instead of redirect so context can be passed
        return render(request, "users/login.html", {
            "message" : "Successfully created account"
        })

    return render(request, "users/signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # check if correct credentials
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "users/login.html", {
                "message": "Invalid credentials"
            })

        login(request, user=user)
        return HttpResponseRedirect(reverse("outfitGenerator:index"))

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/index.html", {
        "message": "Logged out"
    })