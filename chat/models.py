from django.db import models

from django.contrib.auth.models import User


# chatlar uchun model
# bunda biz chat nomini, a'zolarni, xabarlarni saqlaymiz
class Chats(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    members = models.ManyToManyField(User)
    messages = models.ManyToManyField('Messages', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('chat:chat', kwargs={'slug': self.slug})
    
    def get_messages(self):
        return self.messages.all().order_by('created_at')
    
    def get_last_message(self):
        return self.messages.order_by('-created_at').first()
    
    def get_members(self):
        return self.members.all()
    
    def get_members_count(self):
        return self.members.count()
    
    def get_messages_count(self):
        return self.messages.count()


# bu modelda har bir yuborilgan xabar saqlanadi
class Messages(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE, related_name='room', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.text[:50]}'
    
    # def get_absolute_url(self):
    #     return reverse('chat:chat', kwargs={'slug': self.chat.slug})
    
    def get_chat(self):
        return self.chat
    
    def get_author(self):
        return self.author




