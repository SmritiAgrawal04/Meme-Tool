from django.shortcuts import render
from .models import Meme
from django.http import HttpResponse, Http404
from urllib.parse import urlparse
# Create your views here.


# homepage of the webiste
def home(request):
    return (render(request, "home.html"))


def memes(request):
    # when a user submits the upload meme request
    if request.method=='POST':
        # fetch the details entered bythe user
        userName= request.POST['username']
        caption= request.POST['caption']
        imageURL= request.POST['url']

        # save the meme object to the database
        memeObj= Meme()
        memeObj.userName= userName
        memeObj.caption= caption
        memeObj.imageURL= imageURL
        memeObj.save()

        # fetch all the memes from database and display 
        memeObj= Meme.objects.filter()        
        return (render(request, 'view.html', {'memes': memeObj}))

    # when a viewer wants to watch memes
    else:
        # if the mode is mentioned- view/upload
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
    # if the requested id exists render view else 404HTTP
    memeObj= Meme.objects.filter(id=meme_id)   
    if memeObj:
        return (render(request, 'view.html', {'memes': memeObj}))
    else:
        return (render(request, '404Error.html'))

def update(request):
    # when an update request is made for a  meme
    if request.method == 'GET':
        meme_id= request.GET['meme_id']
        memeObj= Meme.objects.filter(id=meme_id)   
        if memeObj:
            return(render(request, "update.html",  {'meme_id': meme_id}))
        else:
            return (render(request, '404Error.html'))
    # when a user submits update request
    else:
        meme_id= request.POST['meme_id']
        if request.POST['memeCaption'] == 'Yes':
            Meme.objects.filter(id=meme_id).update(caption= request.POST['caption'])
        if request.POST['memeImage'] == 'Yes':
            Meme.objects.filter(id=meme_id).update(imageURL= request.POST['url'])

        memeObj= Meme.objects.filter()        
        return (render(request, 'view.html', {'memes': memeObj}))


# increment likes for the meme
def incrementLikes(request):
    meme_id= request.GET['meme_id']
    currentLikes = Meme.objects.filter(id=meme_id)[0].likes
    Meme.objects.filter(id=meme_id).update(likes= currentLikes+1)
    memeObj= Meme.objects.filter()        
    return (render(request, 'view.html', {'memes': memeObj}))