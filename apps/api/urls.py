from django.urls import path

from apps.api import views

urlpatterns = [
    path('places', views.PlacesAPIView.as_view(), name='get_places'),
    path('<int:place_id>/', views.GenerateQRCodeAPIView.as_view(), name='generate_qrcode'),
]