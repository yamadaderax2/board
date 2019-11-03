from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import BoardModel
# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            a = User.objects.get(username = username2)
            return render(request, 'signup.html', {'errorMessage': 'このユーザー名は既に使われています。'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']

        user = authenticate(request, username = username2, password = password2)

        if user is not None:
            login(request, user)
            return redirect('boardapp:list')

        else:
            return render(request, 'login.html', {'loginErrorMessage': 'ログインに失敗しました。'})
    else:
        return render(request, 'login.html')

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    messages.info(request, 'ログアウトしました。')
    return redirect('boardapp:login')
@login_required
def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})

@login_required
def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('boardapp:list')

@login_required
def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    visiter = request.user.get_username()
    readeduser = post.readtext
    if readeduser:
        if visiter in readeduser:
            return redirect('boardapp:list')
    else:
        post.read += 1
        post.readtext = post.readtext+visiter
        post.save()
        return redirect('boardapp:list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('boardapp:list')
