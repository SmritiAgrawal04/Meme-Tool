from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("Hello Meme World!!")
    return (render(request, "home.html"))

def uploadMeme(request):
    return (render(request, 'upload.html'))

def memeTool(request):
    if request.method=='POST':
        return HttpResponse('Hello from POST Method')

    else:
        return HttpResponse('Hello from GET Method')
