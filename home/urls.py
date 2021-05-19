from django.urls import path
from home import views

urlpatterns = [

    path('', views.home_page, name='Home'),
    path('signup/', views.handle_signup, name="handle_signup"),
    path('login/', views.handle_login, name="handle_login"),
    path('logout/', views.handle_logout, name="handle_logout"),

]
