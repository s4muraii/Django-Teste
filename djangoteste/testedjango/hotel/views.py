from django.shortcuts import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("ola mundo")
