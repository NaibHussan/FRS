"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import (index, blog, post, search, special, user_logout,
                         post_create, post_update, post_delete)
from marketing.views import email_list_signup
from upload.views import book_list, upload_book, delete_book
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index),
    path('books/', book_list, name='book_list'),
    path('books/upload/', upload_book, name='upload_book'),
    path('books/<int:pk>/', delete_book, name='delete_book'),
    path('blog/', blog ,name ='post-list'),
    path('search/', search, name = 'search'),
    path('email_list_signup/', email_list_signup, name='email_list_signup'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post,name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='index'),
    path('special/', special, name='special'),
    path('posts/', include('posts.urls')),
    path('logout/', user_logout, name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)   
