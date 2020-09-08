from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about-us',views.about,name='about-us'),
    path('shop',views.shop,name='shop'),
    path('contatc',views.contact,name='contact')
]