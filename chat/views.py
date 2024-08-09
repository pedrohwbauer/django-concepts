from django.shortcuts import render
from django.template.loader import render_to_string
from django.http.response import StreamingHttpResponse
from .models import Message
from time import sleep
# Create your views here.
def index(request):
    messages = Message.objects.all()

    return render(request, 'chat.html', {'messages': messages})

def create_user_message(request):
    content = request.POST.get('content')
    print('content',content)
    user_message = Message(role=Message.USER, content=content)
    def streaming_content():
        message_html = (
            render_to_string('components/user_message.html', context={'message': user_message})
            +
            render_to_string('components/assistant_message.html', context={'current': 'current'})
        )

        print(message_html)
        yield message_html
        
        for i in range(30):
            sleep(1)
            yield f'step {i},'

    return StreamingHttpResponse(streaming_content())

