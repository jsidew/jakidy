from django.core.context_processors import get_token
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {'ctoken': get_token(request)})
