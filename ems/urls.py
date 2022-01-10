from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ems/<str:pk>/', views.single_tag, name='enquiry'),
    path('add-enquiry/', views.create_enquiry, name='create-enquiry'),
    path('update-enquiry/<str:pk>',views.update_enquiry, name='update-enquiry'),
]
