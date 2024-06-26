from django.urls import path
from .views import login_, register_, index, logout_



urlpatterns = [
    path('login/', login_, name='login'),
    path('register/', register_, name='register'),
    path('logout/', logout_, name='logout'),
    path('', index, name='index')
]
