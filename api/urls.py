from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('', views.get_routes),
    path('enquiry/', views.get_ems),
    path('enquiry/<str:pk>', views.get_single_enquiry),
    #path('enquiry/<str:pk>/description', views.enquiry_vote),
]
