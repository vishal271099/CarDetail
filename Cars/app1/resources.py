from .models import CarPerfomance, Car, CarDimension, CarFeature, CarSafety
from import_export import resources, fields


class CarResource(resources.ModelResource):
    brand = fields.Field()
    model_name = fields.Field()
    year = fields.Field()
    color = fields.Field()
    description = fields.Field()
    price = fields.Field()

    class Meta:
        models = Car
        fields = (
            'brand', 'model_name', 'year', 'color', 'description', 'price'
        )
        export_order = (
            'brand', 'model_name', 'year', 'color', 'description', 'price'
        )

    def dehydrate_brand(self, obj):
        try:
            return obj.brand
        except:
            return "N/A"
        
    def dehydrate_model_name(self, obj):
        try:
            return obj.model_name
        except:
            return "N/A"
        
    def dehydrate_year(self, obj):
        try:
            return obj.year
        except:
            return "N/A"
        
    def dehydrate_color(self, obj):
        try:
            return obj.color
        except:
            return "N/A"
        
    def dehydrate_description(self, obj):
        try:
            return obj.description
        except:
            return "N/A"

    def dehydrate_price(self, obj):
        try:
            return obj.price
        except:
            return "N/A"


class CarDimensionResource(resources.ModelResource):
    car_name = fields.Field()
    length = fields.Field()
    width = fields.Field()
    height = fields.Field()

    class Meta:
        models = CarDimension
        fields = (
            'car_name', 'length', 'width', 'height')
        export_order = (
            'car_name', 'length', 'width', 'height')

    def dehydrate_car_name(self, obj):
        try:
            return obj.car_name
        except:
            return "N/A"
        
    def dehydrate_length(self, obj):
        try:
            return obj.length
        except:
            return "N/A"
        
    def dehydrate_width(self, obj):
        try:
            return obj.width
        except:
            return "N/A"
        
    def dehydrate_height(self, obj):
        try:
            return obj.height
        except:
            return "N/A"
        
class CarPerformanceResource(resources.ModelResource):
    car_name = fields.Field()
    engine_capacity = fields.Field()
    acceleration = fields.Field()
    top_speed = fields.Field()
    fuel_economy = fields.Field()

    class Meta:
        models = CarPerfomance
        fields = (
            'car_name', 'engine_capacity', 'acceleration', 'top_speed', 'fuel_economy')
        export_order = (
            'car_name', 'engine_capacity', 'acceleration', 'top_speed', 'fuel_economy')

    def dehydrate_car_name(self, obj):
        try:
            return obj.car_name
        except:
            return "N/A"
        
    def dehydrate_engine_capacity(self, obj):
        try:
            return obj.engine_capacity
        except:
            return "N/A"
        
    def dehydrate_acceleration(self, obj):
        try:
            return obj.acceleration
        except:
            return "N/A"
        
    def dehydrate_top_speed(self, obj):
        try:
            return obj.top_speed
        except:
            return "N/A"
        
    def dehydrate_fuel_economy(self, obj):
        try:
            return obj.fuel_economy
        except:
            return "N/A"
        
class CarSafetyResource(resources.ModelResource):
    car_name = fields.Field()
    airbags = fields.Field()
    width = fields.Field()
    total_number_of_airbags = fields.Field()
    antilock_braking_system = fields.Field()
    electronic_stability_control = fields.Field()
    rearview_camera = fields.Field()

    class Meta:
        models = Car
        fields = (
                'car_name', 'airbags', 'total_number_of_airbags', 'antilock_braking_system', 'electronic_stability_control',
                'rearview_camera'
        )
        export_order = (
                'car_name', 'airbags', 'total_number_of_airbags', 'antilock_braking_system', 'electronic_stability_control',
                'rearview_camera'
        )
    def dehydrate_car_name(self, obj):
        try:
            return obj.car_name
        except:
            return "N/A"
        
    def dehydrate_airbags(self, obj):
        try:
            return obj.airbags
        except:
            return "N/A"
        
    def dehydrate_total_number_of_airbags(self, obj):
        try:
            return obj.total_number_of_airbags
        except:
            return "N/A"
        
    def dehydrate_antilock_braking_system(self, obj):
        try:
            return obj.antilock_braking_system
        except:
            return "N/A"
        
    def dehydrate_electronic_stability_control(self, obj):
        try:
            return obj.electronic_stability_control
        except:
            return "N/A"
        
    def dehydrate_rearview_camera(self, obj):
        try:
            return obj.rearview_camera
        except:
            return "N/A"
        
class CarFeatureResource(resources.ModelResource):
    car_name = fields.Field()
    electronic_parking_brake = fields.Field()
    automatic_parking_assist = fields.Field()
    night_vision_assist = fields.Field()
    adaptive_cruise_control = fields.Field()
    digital_cockpit = fields.Field()
    blind_spot_monitor = fields.Field()
    hill_assist = fields.Field()
    tyre_pressure_monitoring_system = fields.Field()
    automatic_climate_control = fields.Field()
    dual_zone_climate_control = fields.Field()
    anti_pinch_power_windows = fields.Field()
    heated_orvm = fields.Field()
    hill_descent_control = fields.Field()
    apple_car_play = fields.Field()
    hands_free_tailgate = fields.Field()
    mild_hybrid = fields.Field()
    driving_mode = fields.Field()
    real_time_vehicle_tracking = fields.Field()
    engine_immobilizer = fields.Field()

    class Meta:
        models = CarFeature
        fields = ('car_name', 'electronic_parking_brake', 'automatic_parking_assist', 'night_vision_assist', 'adaptive_cruise_control', 'digital_cockpit',
                    'blind_spot_monitor', 'hill_assist', 'tyre_pressure_monitoring_system', 'automatic_climate_control', 'dual_zone_climate_control',
                    'anti_pinch_power_windows', 'heated_orvm', 'hill_descent_control', 'apple_car_play', 'hands_free_tailgate', 'mild_hybrid', 'driving_mode',
                    'real_time_vehicle_tracking', 'engine_immobilizer')
        export_order = ('car_name', 'electronic_parking_brake', 'automatic_parking_assist', 'night_vision_assist', 'adaptive_cruise_control', 'digital_cockpit',
                    'blind_spot_monitor', 'hill_assist', 'tyre_pressure_monitoring_system', 'automatic_climate_control', 'dual_zone_climate_control',
                    'anti_pinch_power_windows', 'heated_orvm', 'hill_descent_control', 'apple_car_play', 'hands_free_tailgate', 'mild_hybrid', 'driving_mode',
                    'real_time_vehicle_tracking', 'engine_immobilizer')
        
    def dehydrate_car_name(self, obj):
        try:
            return obj.car_name
        except:
            return "N/A"
        
    def dehydrate_electronic_parking_brake(self, obj):
        try:
            return obj.electronic_parking_brake
        except:
            return "N/A"
        
    def dehydrate_automatic_parking_assist(self, obj):
        try:
            return obj.automatic_parking_assist
        except:
            return "N/A"
        
    def dehydrate_night_vision_assist(self, obj):
        try:
            return obj.night_vision_assist
        except:
            return "N/A"
        
    def dehydrate_adaptive_cruise_control(self, obj):
        try:
            return obj.adaptive_cruise_control
        except:
            return "N/A"
        
    def dehydrate_digital_cockpit(self, obj):
        try:
            return obj.digital_cockpit
        except:
            return "N/A"
        
       
    def dehydrate_blind_spot_monitor(self, obj):
        try:
            return obj.blind_spot_monitor
        except:
            return "N/A"
        
    def dehydrate_hill_assist(self, obj):
        try:
            return obj.hill_assist
        except:
            return "N/A"
        
    def dehydrate_tyre_pressure_monitoring_system(self, obj):
        try:
            return obj.tyre_pressure_monitoring_system
        except:
            return "N/A"
        
    def dehydrate_automatic_climate_control(self, obj):
        try:
            return obj.automatic_climate_control
        except:
            return "N/A"
        
    def dehydrate_dual_zone_climate_control(self, obj):
        try:
            return obj.dual_zone_climate_control
        except:
            return "N/A"
        
    def dehydrate_anti_pinch_power_windows(self, obj):
        try:
            return obj.anti_pinch_power_windows
        except:
            return "N/A"

        
    def dehydrate_heated_orvm(self, obj):
        try:
            return obj.heated_orvm
        except:
            return "N/A"
        
    def dehydrate_hill_descent_control(self, obj):
        try:
            return obj.hill_descent_control
        except:
            return "N/A"
        
    def dehydrate_apple_car_play(self, obj):
        try:
            return obj.apple_car_play
        except:
            return "N/A"
        
    def dehydrate_hands_free_tailgate(self, obj):
        try:
            return obj.hands_free_tailgate
        except:
            return "N/A"
        
    def dehydrate_mild_hybrid(self, obj):
        try:
            return obj.mild_hybrid
        except:
            return "N/A"
        
    def dehydrate_driving_mode(self, obj):
        try:
            return obj.driving_mode
        except:
            return "N/A"
        
    def dehydrate_real_time_vehicle_tracking(self, obj):
        try:
            return obj.real_time_vehicle_tracking
        except:
            return "N/A"
        
    def dehydrate_engine_immobilizer(self, obj):
        try:
            return obj.engine_immobilizer
        except:
            return "N/A"
        
