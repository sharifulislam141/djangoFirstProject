from django.urls import path 
from ecommerceapp import views

urlpatterns = [
    path('',  views.index),
    path('contact',  views.contact ),
    path('about',  views.about ),
 
]