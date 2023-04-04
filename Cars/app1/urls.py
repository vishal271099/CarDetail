from django.urls import path
from .views import *
urlpatterns = [

    # login API-----------------------------
    path("car/register/", RegisterAPIView.as_view(), name='register'),
    path('car/login/', LoginAPIView.as_view(), name='login'),
    path("car/logout/", LogoutAPIView.as_view(), name='logout'),

    # GET ALL DETAIL API-----------------------------
    path('car/', CarView.as_view(), name='car'),
    path('car/dimension/', CarDimensionView.as_view(), name='car_dimension'),
    path('car/feature/', CarFeatureView.as_view(), name='car_feature'),
    path('car/performance/', CarPerformanceView.as_view(), name='car_performance'),
    path('car/safety/', CarSafetyView.as_view(), name='car_safety'),

    # GET SINGLE ID DATA--------------------
    path('car/<int:pk>/', CarView.as_view(), name='car'),
    path('car/dimension/<int:pk>/', CarDimensionView.as_view(), name='car_dimension'),
    path('car/feature/<int:pk>/', CarFeatureView.as_view(), name='car_feature'),
    path('car/performance/<int:pk>/', CarPerformanceView.as_view(), name='car_performance'),
    path('car/safety/<int:pk>/', CarSafetyView.as_view(), name='car_safety'),

    # Export API---------------------------
    path('export/car_export', ExportCarView.as_view(), name='export_car'),

]
