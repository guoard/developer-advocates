from django.urls import path

from . import views

urlpatterns = [
    path('', views.advocate_list, name='advocate-list'),
    path('<int:id>/', views.advocate_detail, name='advocate-detail'),
]
