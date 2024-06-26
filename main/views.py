from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from chat.models import Chats

# bosh sahifa
# bu yerda barcha chatlar ko'rinadi va yangi yaratish ham mumkin
def index(request):
    chats = Chats.objects.all().order_by('-created_at')
    context = {
        'chats': chats
    }
    return render(request=request, template_name="index.html", context=context)


# user tizimga kirishi uchun
def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# yangi userni ro'yxatdan o'tkazish
def register_(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# tizimdan chiqish
def logout_(request):
    logout(request)
    return redirect('index')