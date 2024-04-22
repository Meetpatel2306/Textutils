"""
URL configuration for textutils project.

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
# from django.contrib import admin
# from django.urls import path
# from . import views

# code for video 6
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('about',views.about,name='about')
# ]

# code for video 7
# urlpatterns = [
#      path('admin/', admin.site.urls),
#      path('',views.index,name='index'),

    #  video 7
    #  path('removepunc',views.removepunc,name='removep'),
    #  path('capitalizefirst',views.capitalizefirst,name='capfirst'),
#     #  path('newlineremove', views.newlineremove, name='newlineremove'),
#     #  path('spaceremover', views.spaceremover, name='spaceremover'),
#     # path('charcounter',views.charcounter,name='charcounter'),
#
# # video 9 text box banavanu and button tag and button dabao to charcounter page khule
#      path('charcounter',views.charcounter,name='charcounter'),

# video 10
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   path('analyze', views.analyze, name='analyze'),
   # path('exercise1',views.exercise1,name='exercise1')
]
