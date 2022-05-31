from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('category/', views.category, name='category')
]