from django.shortcuts import render
from .models import Meme
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("Hello Meme World!!")
    return (render(request, "home.html"))

def uploadMeme(request):
    return (render(request, 'upload.html'))

def viewMeme(request):
    return (render(request, 'view.html'))

def memeTool(request):
    if request.method=='POST':
        userName= request.POST['username']
        caption= request.POST['caption']
        imageURL= request.POST['url']
        print (userName, caption, imageURL)

        memeObj= Meme()
        memeObj.userName= userName
        memeObj.caption= caption
        memeObj.imageURL= imageURL

        memeObj.save()

        memeObj= Meme.objects.filter()        
        return (render(request, 'view.html', {'memes': memeObj}))

    else:
        memeObj= Meme.objects.filter()        
        return (render(request, 'view.html', {'memes': memeObj}))
