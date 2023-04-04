from django.db import models
from django.utils.translation import gettext as _

class Car(models.Model):
    brand = models.CharField(_('Brand'),max_length=100, db_index=True, null=True, blank=True)
    model_name = models.CharField(_('Model Name'), max_length=100, db_index=True, null=True, blank=True)
    year = models.PositiveIntegerField(_('Year'), db_index=True, null=True, blank=True)
    color = models.CharField(_('Color'), max_length=50, db_index=True, null=True, blank=True)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2, db_index=True, null=True, blank=True)
    description = models.TextField(_('Description'), db_index=True, null=True, blank=True)
    image = models.ImageField(_('Image'), upload_to='images/')

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):   
        return f'{self.brand}'

# Car dimensions
class CarDimension(models.Model):
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    length = models.PositiveIntegerField(_('Length'), db_index=True, null=True, blank=True)
    width = models.PositiveIntegerField(_('Width'), db_index=True, null=True, blank=True)
    height = models.PositiveIntegerField(_('Height'), db_index=True, null=True, blank=True)

    class Meta:
        verbose_name = "Car Dimension"
        verbose_name_plural = "Car Dimensions"

    def __str__(self):
        return f'{self.car_name}'


# Car performance details
class CarPerfomance(models.Model):
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    engine_capacity = models.DecimalField(_('Engine Capacity'), max_digits=4, decimal_places=1, db_index=True, null=True, blank=True)
    acceleration = models.PositiveIntegerField(_('Acceleration'), db_index=True, null=True, blank=True)
    top_speed = models.PositiveIntegerField(_('Top Speed'), db_index=True, null=True, blank=True)
    fuel_economy = models.DecimalField(_('Fuel Economy'), max_digits=4, decimal_places=2, db_index=True, null=True, blank=True)

    class Meta:
        verbose_name = "Car Perfomance"
        verbose_name_plural = "Car Perfomances"

    def __str__(self):
        return f'{self.car_name}'
    

# Car safety details
class CarSafety(models.Model):
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    airbags = models.PositiveIntegerField(_('Airbags'), db_index=True, null=True, blank=True)
    total_number_of_airbags = models.PositiveIntegerField(_(' Total Number of Airbags'), db_index=True, null=True, blank=True)
    antilock_braking_system = models.BooleanField(_('ABS'), db_index=True, null=True, blank=True)
    electronic_stability_control = models.BooleanField(default=False, help_text="electronic stability control supported or not.")
    rearview_camera = models.BooleanField(default=False, help_text="rearview camera supported or not.")

    class Meta:
        verbose_name = "Car Safety"
        verbose_name_plural = "Car Safeties"

    def __str__(self):
        return f"{self.car_name}"
    
# Car features List
class CarFeature(models.Model):
    car_name = models.ForeignKey(Car, related_name='feature_of_car', on_delete=models.CASCADE)
    electronic_parking_brake = models.BooleanField(default=False, help_text="electronic_parking_brake supported or not.")
    automatic_parking_assist = models.BooleanField(default=False, help_text="automatic_parking_assist supported or not.")
    night_vision_assist = models.BooleanField(default=False, help_text="night_vision_assist supported or not.")
    adaptive_cruise_control = models.BooleanField(default=False, help_text="adaptive_cruise_control supported or not.")
    digital_cockpit = models.BooleanField(default=False, help_text="digital_cockpit supported or not.")
    blind_spot_monitor = models.BooleanField(default=False, help_text="blind_spot_monitor supported or not.")
    hill_assist = models.BooleanField(default=False, help_text="hill_assist supported or not.")
    tyre_pressure_monitoring_system = models.BooleanField(default=False, help_text="tyre_pressure_monitoring_system supported or not.")
    automatic_climate_control = models.BooleanField(default=False, help_text="automatic_climate_control supported or not.")
    dual_zone_climate_control = models.BooleanField(default=False, help_text="dual_zone_climate_control supported or not.")
    anti_pinch_power_windows = models.BooleanField(default=False, help_text="anti_pinch_power_windows supported or not.")
    heated_orvm = models.BooleanField(default=False, help_text="heated_orvm supported or not.")
    hill_descent_control = models.BooleanField(default=False, help_text="hill_descent_control supported or not.")
    apple_car_play = models.BooleanField(default=False, help_text="apple_car_play supported or not.")
    hands_free_tailgate = models.BooleanField(default=False, help_text="hands_free_tailgate supported or not.")
    mild_hybrid = models.BooleanField(default=False, help_text="mild_hybrid supported or not.")
    driving_mode = models.BooleanField(default=False, help_text="driving_mode supported or not.")
    real_time_vehicle_tracking = models.BooleanField(default=False, help_text="real_time_vehicle_tracking supported or not.")
    engine_immobilizer = models.BooleanField(default=False, help_text="engine_immobilizer supported or not.")

    class Meta:
        verbose_name = "Car Feature"
        verbose_name_plural = "Car Features"

    def __str__(self):
        return f"{self.car_name})"