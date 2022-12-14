"""redditclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts', views.PostList.as_view(), name='posts'),
    path('api/posts/<int:pk>', views.PostRetrieveDestroy.as_view(), name='posts_destroy'),
    path('api/posts/<int:pk>/vote', views.VoteCreate.as_view(), name='vote'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/signup', views.signup),
    path('api/login', views.login)
]
