from django.urls import path
from . import views

urlpatterns = [
    path('get-in-touch',views.contact,name='contact'),
]