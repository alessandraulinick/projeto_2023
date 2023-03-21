from django.urls import path
from . import views

from .views import index, contato, produto

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/<int:id>/', views.produto, name='produto'),
]