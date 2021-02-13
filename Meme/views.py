from django.shortcuts import render
from .models import Meme
from django.http import HttpResponse, Http404
from urllib.parse import urlparse
# Create your views here.
def home(request):
    return (render(request, "home.html"))

def memes(request):
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
        try:
            mode= request.GET['mode']
            if mode == 'upload':
                return (render(request, 'upload.html'))
            elif mode == 'view':
                memeObj= Meme.objects.filter()        
                return (render(request, 'view.html', {'memes': memeObj}))
            else:
                pass
        except:
            pass
    
def specialRequest(request, meme_id):
    memeObj= Meme.objects.filter(id=meme_id)   
    if memeObj:
        return (render(request, 'view.html', {'memes': memeObj}))
    else:
        return (render(request, '404Error.html'))

    