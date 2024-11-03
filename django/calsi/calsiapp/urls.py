
from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.home, name='homepage'),
    path('contact',views.contact,name='contact'),
    path('add',views.add,name='add'),
]
