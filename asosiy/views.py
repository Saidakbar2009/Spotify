from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .serializer import *
# Create your views here.
# class QoshiqchiListAPIView(APIView):
#     def get(self, request, format=None):
#         qoshiqchis = Qoshiqchi.objects.all()
#         serializer = QoshiqchiSerializer(qoshiqchis, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = QoshiqchiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
# class QoshiqchiApi(APIView):
#     def get(self, request, pk):
#         qoshiqchi = Qoshiqchi.objects.get(id=pk)
#         serializer = QoshiqchiSerializer(qoshiqchi)
#         return Response(serializer.data)
    
#     def update(self, request, pk):
#         data = request.data
#         qoshiqchi = Qoshiqchi.objects.filter(id=pk)
#         serializer = Qoshiqchi(qoshiqchi, data=data)
#         if serializer.is_valid():
#             valid = serializer.validated_data
#             qoshiqchi.update(
#                 ism = valid.get('ism'),
#                 tugilgan_yil = valid.get('tugilgan_yil'),
#                 davlat = valid.get('davlat')
#             )
#             return Response({'success': 'True'})
#         return Response(serializer.errors) 
    
#     def delete(self, request, pk):
#         Qoshiqchi.objects.get(id=pk).delete()
#         return Response({"success": 'True'})
    
class AlbomModelViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nom']
    ordering_fields = ['sana']
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

class QoshiqchiModelViewSet(viewsets.ModelViewSet):
    qidiruv = request.query_params.get('qidiruv')
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['ism', 'davlat']
    ordering_fields = ['tugilgan_yil']
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

class QoshiqModelViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['davomiylik']
    search_fields = ['nom', 'janr']
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer