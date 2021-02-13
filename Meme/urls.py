from django.urls import path, re_path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('memes', views.memes, name= 'memes'),
    # re_path(r'memes/$', views.specialRequest, name='specialRequest')
    # url('memes/<int:id>', views.specialRequest, name = 'specialRequest'),
    url(r'^memes/(?P<meme_id>\d+)/$', views.specialRequest, name='specialRequest')
    # url(r'^users/(?P<user_id>\d+)/$', 'viewname', name='urlname')

]
