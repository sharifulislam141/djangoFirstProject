from django.urls import path
from authe import views

urlpatterns = [
    path('login/',views.handlelogin , name= "handleLogin"),
    path('logout/',views.handlelogout , name= "handleout"),
    path('signin/',views.signin , name= "signin"),
    path('activate/<uid64>/<token>',views.ActivateAccountView.as_view(),name = 'activate')
   
]