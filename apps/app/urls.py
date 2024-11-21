from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('place/<int:id>/', views.detail_page, name='detail_page'),

    path('/payment/<int:id>/', views.payment_page, name='payment_page'),
]
