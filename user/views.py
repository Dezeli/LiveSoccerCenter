from django.shortcuts import render
from .models import User
from post.models import Post
from user.forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "user/index.html")


def signup_page(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["ID"]
            if User.objects.filter(username=user_id).exists():
                messages.info(request, "이미 존재하는 유저이름입니다.")
            elif form.cleaned_data["PW"] != form.cleaned_data["PW_C"]:
                messages.info(request, "비밀번호가 서로 일치하지 않습니다.")
            else:
                user_pw = form.cleaned_data["PW"]
                first_name = form.cleaned_data["first_name"]
                add_list = User(username=user_id, first_name=first_name)
                add_list.set_password(user_pw)
                add_list.save()
                messages.info(request, "회원가입이 정상적으로 완료되었습니다.")
                return HttpResponseRedirect(reverse("post:index"))

    form = SignupForm()
    return render(request, "user/signup.html", {"form": form})


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["ID"]
            user_pw = form.cleaned_data["PW"]
            user = authenticate(request, username=user_id, password=user_pw)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("post:index"))
            else:
                messages.info(request, "아이디가 없거나 비밀번호가 잘못되었습니다.")
                return HttpResponseRedirect(reverse("user:login"))

    form = LoginForm()
    return render(request, "user/login.html", {"form": form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("post:index"))
