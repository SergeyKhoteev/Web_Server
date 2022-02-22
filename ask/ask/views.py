from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request, *args, **kwargs):
    return HttpResponse('OK')

# Create your views here.
