from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('auth', views.auth, name='auth'),
    path('reg', views.registretion_view, name='reg'),
    path('changes/<int:change_id>', views.change_detail, name='ch_detail_url'),
]