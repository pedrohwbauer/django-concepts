from django.urls import path
from chat.consumers import ChatConsumer
urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
]