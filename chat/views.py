from django.shortcuts import render, get_object_or_404, redirect

from rest_framework import viewsets
from .models import Messages, Chats
from .serializers import MessageSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer


# chatga kirish
# bunda foydalanuvchidan tizimga kirgan bo'lishi talab etiladi
@login_required(login_url='/login/')
def enter_chat(request, chat_id):
    chat = get_object_or_404(Chats, id=chat_id)
    messages = Messages.objects.filter(chat=chat)
    context = {
        'messages': messages,
        'chat': chat
    }

    return render(request, "chat.html", context=context)


# chatga a'zo bo'lish
# chatda xabarlar yozish uchun a'zob bo'lish kerak
# bunda ham user tizimga kirgan bo'lishi kerak
@login_required(login_url='/login/')
@require_POST
def join_chat(request, chat_id):
    chat = get_object_or_404(Chats, id=chat_id)
    chat.members.add(request.user)
    return JsonResponse({'status': 'joined'})


# yangi chat yaratish
@login_required(login_url='/login/')
@require_POST
def create_chat(request):
    chat_name = request.POST.get('chat_name')
    if chat_name:
        chat = Chats.objects.create(name=chat_name)
        chat.members.add(request.user)
        return redirect('enter_chat', chat.id)
    
    return redirect('index')