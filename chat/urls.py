from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, enter_chat, join_chat, create_chat

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('chat/<int:chat_id>/join/', join_chat, name='join_chat'),
    path('chat/create/', create_chat, name='create_chat'),
    path('chat/<int:chat_id>/', enter_chat, name="enter_chat"),
    path('chat/api/', include(router.urls)),
]
