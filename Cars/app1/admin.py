from django.contrib import admin
from .models import Car, CarDimension, CarFeature, CarPerfomance, CarSafety
from import_export.admin import ExportMixin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from .resources import *

# Register your models here.
class CarAdmin(ExportMixin,  ForeignKeyAutocompleteAdmin):
    resource_class = CarResource
    list_display = ('brand', 'model_name', 'year', 'color', 'price', 'description', 'image')
    search_fields = ['brand', 'model_name', 'year', 'price']
    list_filter = ['brand', 'year']

class CarDimensionAdmin(ExportMixin,  ForeignKeyAutocompleteAdmin):
    resource_class = CarDimensionResource
    list_display = ('car_name', 'length', 'width', 'height')
    search_fields = ['car_name', 'length', 'width', 'height']
    # list_filter = ['car_name']

class CarPerfomanceAdmin(ExportMixin,  ForeignKeyAutocompleteAdmin):
    resource_class = CarPerformanceResource
    list_display = ('car_name', 'engine_capacity', 'acceleration', 'top_speed', 'fuel_economy')
    search_fields = ['car_name']
    # list_filter = ['car_name']


class CarSafetyAdmin(ExportMixin,  ForeignKeyAutocompleteAdmin):
    resource_class = CarSafetyResource
    list_display = ('car_name', 'airbags', 'total_number_of_airbags', 'antilock_braking_system', 'electronic_stability_control', 'rearview_camera')
    search_fields = ['car_name']
    # list_filter = ['car_name']

class CarFeatureAdmin(ExportMixin,  ForeignKeyAutocompleteAdmin):
    resource_class = CarFeatureResource
    list_display = ('car_name', 'electronic_parking_brake', 'automatic_parking_assist', 'night_vision_assist', 'adaptive_cruise_control', 'digital_cockpit',
                    'blind_spot_monitor', 'hill_assist', 'tyre_pressure_monitoring_system', 'automatic_climate_control', 'dual_zone_climate_control',
                    'anti_pinch_power_windows', 'heated_orvm', 'hill_descent_control', 'apple_car_play', 'hands_free_tailgate', 'mild_hybrid', 'driving_mode',
                    'real_time_vehicle_tracking', 'engine_immobilizer')
    search_fields = ['car_name']
    # list_filter = ['car_name']


    

admin.site.register(Car, CarAdmin)
admin.site.register(CarFeature, CarFeatureAdmin)
admin.site.register(CarDimension, CarDimensionAdmin)
admin.site.register(CarPerfomance, CarPerfomanceAdmin)
admin.site.register(CarSafety, CarSafetyAdmin)
