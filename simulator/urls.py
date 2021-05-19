from django.urls import path
from simulator import views

urlpatterns = [

    path('', views.handle_simulator, name='Simulator'),
    path('output/', views.handle_output, name='Output'),
]
