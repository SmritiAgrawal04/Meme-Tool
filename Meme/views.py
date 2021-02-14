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
                return (render(request, '404Error.html'))
        except:
            return (render(request, '404Error.html'))
    
def specialRequest(request, meme_id):
    memeObj= Meme.objects.filter(id=meme_id)   
    if memeObj:
        return (render(request, 'view.html', {'memes': memeObj}))
    else:
        return (render(request, '404Error.html'))

def update(request):
    if request.method == 'GET':
        meme_id= request.GET['meme_id']
        memeObj= Meme.objects.filter(id=meme_id)   
        if memeObj:
            return(render(request, "update.html",  {'meme_id': meme_id}))
        else:
            return (render(request, '404Error.html'))
    else:
        meme_id= request.POST['meme_id']
        if request.POST['memeCaption'] == 'Yes':
            Meme.objects.filter(id=meme_id).update(caption= request.POST['caption'])
        if request.POST['memeImage'] == 'Yes':
            Meme.objects.filter(id=meme_id).update(imageURL= request.POST['url'])

        memeObj= Meme.objects.filter()        
        return (render(request, 'view.html', {'memes': memeObj}))


def incrementLikes(request):
    meme_id= request.GET['meme_id']
    currentLikes = Meme.objects.filter(id=meme_id)[0].likes
    Meme.objects.filter(id=meme_id).update(likes= currentLikes+1)
    memeObj= Meme.objects.filter()        
    return (render(request, 'view.html', {'memes': memeObj}))