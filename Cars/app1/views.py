from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from django.contrib.auth import login, logout
from .tasks import send_mail_task
import io
from .utils import *
from django.http import HttpResponse
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters.rest_framework
from django.db.models import Q, F


# All Car details----------------------------------------------.
class CarView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    api_view = ['GET', 'POST', 'PUT', 'DELETE']
    serializer_class = CarSerializer
    filter_backends = [SearchFilter, django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    ordering_fields = ('year', 'brand', 'color', 'price', 'model_name')


    # Custom ordering fucntion for fields-------------------------------------
    def get_queryset(self):
        car = Car.objects.all()
        try:
            if self.request.query_params.get('ordering') in ['year', '-year']:
                return car.order_by(self.request.query_params.get('ordering'))
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
        try:
            if self.request.query_params.get('ordering') in ['brand', '-brand']:
                return car.order_by(self.request.query_params.get('ordering'))
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
        try:
            if self.request.query_params.get('ordering') in ['color', '-color']:
                return car.order_by(self.request.query_params.get('ordering'))
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
        try:
            if self.request.query_params.get('ordering') in ['price', '-price']:
                return car.order_by(self.request.query_params.get('ordering'))
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
        try:
            if self.request.query_params.get('ordering') in ['model_name', '-model_name']:
                return car.order_by(self.request.query_params.get('ordering'))
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        return car

    def get(self, request, pk=None):
        try:
            if pk:
                print("iddddd", id)
                obj = Car.objects.get(id=pk)
                serialized =CarSerializer(obj)
                return Response({'car': serialized.data}, status=status.HTTP_200_OK)
            obj = self.get_queryset()
            print('yyyyy', obj)
            serialized = CarSerializer(obj, many=True)
            return Response({'car': serialized.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            car = request.data
            serializer = CarSerializer(data=car)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'car': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data added successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            saved_car = Car.objects.filter(pk=pk).last()
            data = request.data
            serializer = CarSerializer(instance=saved_car, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'car': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            detail = Car.objects.filter(id=pk)
            detail.delete()
            return Response({'success': 'data deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        

# All Car  Dimension details----------------------------------------------.
class CarDimensionView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    api_view = ['GET', 'POST', 'PUT', 'DELETE']
    serializer_class = CarDimensionSerializer

    def get(self, request, pk=None):
        try:
            if pk:
                obj = CarDimension.objects.get(id=pk)
                serialized = CarDimensionSerializer(obj) 
                return Response({'Car Dimension': serialized.data}, status=status.HTTP_200_OK)              
            obj = CarDimension.objects.all()
            serialized = CarDimensionSerializer(obj, many=True)
            return Response({'Car Dimension': serialized.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            car_dimension = request.data
            serializer = self.serializer_class(data=car_dimension)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'car_dimension': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data added successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        try:
            saved_car = CarDimension.objects.filter(pk=pk).last()
            data = request.data
            serializer = CarDimensionSerializer(instance=saved_car, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'Car Dimension': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response([], status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            detail = CarDimension.objects.filter(id=pk)
            detail.delete()
            return Response({'success': 'data deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)


# All Car Performance details----------------------------------------------.
class CarPerformanceView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    api_view = ['GET', 'POST','PUT','DELETE']
    serializer_class = CarPerfomanceSerializer

    def get(self, request, pk=None):
        try:
            if pk:
                obj=CarPerfomance.objects.get(id=pk)
                serialized = CarPerfomanceSerializer(obj)
                return Response({'car performance' :serialized.data}, status=status.HTTP_200_OK)
            obj = CarPerfomance.objects.all()
            serialized = CarPerfomanceSerializer(obj, many=True)
            return Response({'car performance' :serialized.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)

    
    def post(self, request):
        try:
            car_performance = request.data
            serializer = self.serializer_class(data=car_performance)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'car_performance': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data added successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        try:
            saved_car = CarPerfomance.objects.filter(pk=pk).last()
            data = request.data
            serializer = CarPerfomanceSerializer(instance=saved_car, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'Car Performance': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            detail = CarPerfomance.objects.filter(id=pk)
            detail.delete()
            return Response({'success': 'data deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    

# All Car Safety details----------------------------------------------.
class CarSafetyView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    api_view = ['GET', 'POST', 'PUT', 'DELETE']
    serializer_class = CarSafetySerializer

    def get(self, request, pk=None):
        try:
            if pk:
                obj = CarSafety.objects.get(id=pk)
                serialized = CarSafetySerializer(obj)
                return Response({'car safety' :serialized.data}, status=status.HTTP_200_OK) 
            obj = CarSafety.objects.all()
            serialized = CarSafetySerializer(obj, many=True)
            return Response({'car safety' :serialized.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)

    
    def post(self, request):
        try:
            car_safety = request.data
            serializer = self.serializer_class(data=car_safety)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'car_safety': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data added successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        try:
            saved_car = CarSafety.objects.filter(pk=pk).last()
            data = request.data
            serializer = CarSafetySerializer(instance=saved_car, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'Car Safety': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            detail = CarSafety.objects.filter(id=pk)
            detail.delete()
            return Response({'success': 'data deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
    

# All Car Feature details----------------------------------------------.
class CarFeatureView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    api_view = ['GET', 'POST', 'PUT', 'DELETE']
    serializer_class = CarFeatureSerializer

    def get(self, request, pk=None):
        try:
            if pk:
                obj = CarFeature.objects.get(id=pk)
                serialized = CarFeatureSerializer(obj)
                return Response({'car feature' :serialized.data}, status=status.HTTP_200_OK)
            obj = CarFeature.objects.all()
            serialized = CarFeatureSerializer(obj, many=True)
            return Response({'car feature' :serialized.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)

    
    def post(self, request):
        try:
            car_feature = request.data
            serializers=self.serializer_class(data=car_feature)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
                return Response({'car_feature': serializers.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data added successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        

    def put(self, request, pk):
        try:
            saved_car = CarFeature.objects.filter(pk=pk).last()
            data = request.data
            serializer = CarFeatureSerializer(instance=saved_car, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'Car Feature': serializer.data}, status=status.HTTP_200_OK)
            return Response({'success': 'data updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            detail = CarFeature.objects.filter(id=pk)
            detail.delete()
            return Response({'success': 'data deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([], status=status.HTTP_200_OK)
        
# Register API-----------------------------------------------------------------
class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            login(request, user)
            send_mail_task.delay(user.id)
            return Response({"msg": "register successfully"}, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        

# Login API-----------------------------------------------------------------
class LoginAPIView(APIView):
    serializer_class = LoginTokenSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"msg": "login successfully"}, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
# Logout API-----------------------------------------------------------------
class LogoutAPIView(APIView):
    serializer_class = LoginTokenSerializer

    def post(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)


# Export APi for Car-----------------------------------------------------
class ExportCarView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    api_view = ['GET',]

    def get(self, request):
        try:
            file_type = self.request.query_params.get('file_type', 'csv').lower()
            car_data = Car.objects.all()
            output = io.BytesIO()
            serializer = CarSerializer(car_data, many=True)
            sheet = ExportCar(output, file_type).export_sheet_car(serializer.data)
            output.seek(0)
            response = HttpResponse(
                output,
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename= Car.'  + str(file_type)

            return response 
        except Exception as e:
            print(e)
            return Response({'message': "Export Mass Upload Errors Report"}, status=status.HTTP_400_BAD_REQUEST)