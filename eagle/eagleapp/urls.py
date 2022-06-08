from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manhattan/', views.manhattan, name='data'),
    path('bronx/', views.bronx, name='data'),
    path('broklyn/', views.broklyn, name='data'),
    path('queens/', views.queens, name='data'),
]