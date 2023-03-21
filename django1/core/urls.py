from django.urls import path
from core import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/<int:pk>/', views.produto, name='produto'),
]

handler404 = views.error404
handler500 = views.error500