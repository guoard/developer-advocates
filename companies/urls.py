from django.urls import path

from . import views

urlpatterns = [
    path('', views.company_list, name='company-list'),
    path('<int:id>/', views.company_detail, name='company-detail')
]
