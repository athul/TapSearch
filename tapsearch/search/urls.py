from django.urls import path,include
from .views import *
urlpatterns = [
    path('index',index,),
    path('search',search, name="search")
]
