
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from .views import home, sobre, post, fortag

app_name = 'Blog'

urlpatterns = [
    path('', home, name= 'home'),
    path('sobre/', sobre),
    path('post/<int:pk>/', post, name = 'post'),
    path('tag/<slug:slug>/', fortag, name='fortag'),
    path('/ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
