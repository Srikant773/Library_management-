"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from college import views as sview
from home import views as hview
urlpatterns = [
    path('admin/', admin.site.urls),
     path('signup',sview.user,name='signup'),
    path('slogin',sview.slogin,name='slogin'),
    path('shome',sview.qview,name='shome'),
    path('alogin',sview.admin,name='alogin'),
    path('ahome',sview.whome,name='ahome'),
    # path('edit',sview.edit,name='edit'),
    path('addbook',sview.addbook,name='addbook'),
    path('bookissuse',sview.bookissuse,name='bookissuse'),
    path('',hview.home),
    path('issuedetail',sview.issueshow,name='issuedetail'),
    path('logout',sview.logout_view,name='logout'),
    path('slogout',sview.logout_sview,name='slogout'),
 
    path('update',sview.update,name='update')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
