from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework import exceptions
UserModel = get_user_model()

class CarSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(required=True)
    model_name = serializers.CharField()
    year = serializers.IntegerField()
    color = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    image = serializers.ImageField()

    class Meta:
        model = Car
        fields = ['brand', 'model_name','color', 'description', 'image', 'year', 'price']

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model_name = validated_data.get('model_name', instance.model_name)
        instance.year = validated_data.get('year', instance.year)
        instance.color = validated_data.get('color', instance.color)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class CarDimensionSerializer(serializers.ModelSerializer):
    car_name = serializers.CharField(required=True)
    height = serializers.IntegerField()
    length = serializers.IntegerField()
    width = serializers.IntegerField()

    class Meta:
        model = CarDimension
        fields = ['car_name', 'height', 'length', 'width']

    def create(self, validated_data):
        model=Car.objects.get(brand=validated_data['car_name'])
        validated_data['car_name']=model
        return CarDimension.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        car_name = validated_data.pop('car_name')
        instance.car_name.brand = car_name
        instance.height = validated_data.get('height', instance.height)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.save()
        return instance

class CarPerfomanceSerializer(serializers.ModelSerializer):
    car_name = serializers.CharField(required=True)
    engine_capacity = serializers.CharField()
    acceleration = serializers.IntegerField()
    top_speed = serializers.CharField()
    fuel_economy = serializers.IntegerField()

    class Meta:
        model = CarPerfomance
        fields = ['car_name', 'engine_capacity', 'acceleration', 'top_speed', 'fuel_economy']

    def create(self, validated_data):
        model=Car.objects.get(brand=validated_data['car_name'])
        validated_data['car_name']=model
        return CarPerfomance.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        car_name = validated_data.pop('car_name')
        instance.car_name.brand = car_name
        instance.engine_capacity = validated_data.get('engine_capacity', instance.engine_capacity)
        instance.acceleration = validated_data.get('acceleration', instance.acceleration)
        instance.top_speed = validated_data.get('top_speed', instance.top_speed)
        instance.fuel_economy = validated_data.get('fuel_economy', instance.fuel_economy)
        instance.save()
        return instance

class CarSafetySerializer(serializers.ModelSerializer):
    car_name = serializers.CharField(required=True)
    airbags = serializers.CharField()
    total_number_of_airbags = serializers.IntegerField()
    antilock_braking_system = serializers.CharField()
    electronic_stability_control = serializers.BooleanField()
    rearview_camera = serializers.BooleanField()

    class Meta:
        model = CarSafety
        fields = ['car_name', 'airbags', 'total_number_of_airbags', 'antilock_braking_system', 'electronic_stability_control',
                  'rearview_camera']
        
    def create(self, validated_data):
        model=Car.objects.get(brand=validated_data['car_name'])
        validated_data['car_name']=model
        return CarSafety.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        car_name = validated_data.pop('car_name')
        instance.car_name.brand = car_name
        instance.airbags = validated_data.get('airbags', instance.airbags)
        instance.total_number_of_airbags = validated_data.get('total_number_of_airbags', instance.total_number_of_airbags)
        instance.antilock_braking_system = validated_data.get('antilock_braking_system', instance.antilock_braking_system)
        instance.rearview_camera = validated_data.get('rearview_camera', instance.rearview_camera)
        instance.electronic_stability_control = validated_data.get('electronic_stability_control', instance.electronic_stability_control)
        instance.save()
        return instance
        
class CarFeatureSerializer(serializers.ModelSerializer):
    car_name = serializers.CharField(required=True)
    electronic_parking_brake = serializers.BooleanField()
    automatic_parking_assist = serializers.BooleanField()
    night_vision_assist = serializers.BooleanField()
    adaptive_cruise_control = serializers.BooleanField()
    digital_cockpit = serializers.BooleanField()
    hill_assist = serializers.BooleanField()
    tyre_pressure_monitoring_system = serializers.BooleanField()
    automatic_climate_control = serializers.BooleanField()
    dual_zone_climate_control = serializers.BooleanField()
    anti_pinch_power_windows = serializers.BooleanField()
    heated_orvm = serializers.BooleanField()
    hill_descent_control = serializers.BooleanField()
    apple_car_play = serializers.BooleanField()
    hands_free_tailgate = serializers.BooleanField()
    mild_hybrid = serializers.BooleanField()
    driving_mode = serializers.BooleanField()
    real_time_vehicle_tracking = serializers.BooleanField()
    engine_immobilizer = serializers.BooleanField()

    class Meta:
        model = CarFeature
        fields = ['car_name', 'electronic_parking_brake', 'automatic_parking_assist', 'night_vision_assist',
                  'adaptive_cruise_control', 'digital_cockpit', 'hill_assist', 'tyre_pressure_monitoring_system', 'automatic_climate_control',
                  'dual_zone_climate_control', 'anti_pinch_power_windows', 'heated_orvm', 'hill_descent_control', 'apple_car_play',
                  'hands_free_tailgate', 'mild_hybrid', 'driving_mode', 'real_time_vehicle_tracking', 'engine_immobilizer']
        
    def create(self, validated_data):
        model=Car.objects.get(brand=validated_data['car_name'])
        validated_data['car_name']=model
        return CarFeature.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        car_name = validated_data.pop('car_name')
        instance.car_name.brand = car_name
        instance.electronic_parking_brake = validated_data.get('electronic_parking_brake', instance.electronic_parking_brake)
        instance.automatic_parking_assist = validated_data.get('automatic_parking_assist', instance.automatic_parking_assist)
        instance.night_vision_assist = validated_data.get('night_vision_assist', instance.night_vision_assist)
        instance.adaptive_cruise_control = validated_data.get('adaptive_cruise_control', instance.adaptive_cruise_control)
        instance.digital_cockpit = validated_data.get('digital_cockpit', instance.digital_cockpit)
        instance.hill_assist = validated_data.get('hill_assist', instance.hill_assist)
        instance.tyre_pressure_monitoring_system = validated_data.get('tyre_pressure_monitoring_system', instance.tyre_pressure_monitoring_system)
        instance.automatic_climate_control = validated_data.get('automatic_climate_control', instance.automatic_climate_control)
        instance.dual_zone_climate_control = validated_data.get('dual_zone_climate_control', instance.dual_zone_climate_control)
        instance.anti_pinch_power_windows = validated_data.get('anti_pinch_power_windows', instance.anti_pinch_power_windows)
        instance.heated_orvm = validated_data.get('heated_orvm', instance.heated_orvm)
        instance.hill_descent_control = validated_data.get('hill_descent_control', instance.hill_descent_control)
        instance.apple_car_play = validated_data.get('apple_car_play', instance.apple_car_play)
        instance.hands_free_tailgate = validated_data.get('hands_free_tailgate', instance.hands_free_tailgate)
        instance.mild_hybrid = validated_data.get('mild_hybrid', instance.mild_hybrid)
        instance.driving_mode = validated_data.get('driving_mode', instance.driving_mode)
        instance.real_time_vehicle_tracking = validated_data.get('real_time_vehicle_tracking', instance.real_time_vehicle_tracking)
        instance.engine_immobilizer = validated_data.get('engine_immobilizer', instance.engine_immobilizer)
        instance.save()
        return instance
    
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def create(self, validated_data, **extra_fields):
        user = UserModel.objects.create(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            password = self.validated_data['password'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )
        confirm_password = self.validated_data['confirm_password']
        user.set_password('password')
        user.save()
        return user
    
    def validate_password(self,value):
        data = self.get_initial()
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise exceptions.ValidationError('Password must be same')
        return value
    
class LoginTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        msg = ""
        username = attrs.get('username')
        password = attrs.get('password')
        try:
            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    msg = "provide credential is incorrect"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "sorry, your password in incorect"
                raise exceptions.ValidationError(msg)
        except Exception as e:
            print(str(e))
            msg = "user not found"
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs