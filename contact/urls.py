from django.urls import path
from contact import views

urlpatterns = [


    path('', views.handle_contact, name='Contact'),
]
