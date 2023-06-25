from django.urls import path
from . import views

urlpatterns = [
    path('topanime/', views.topanime, name = 'topanime')
]
