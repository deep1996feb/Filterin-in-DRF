from django.shortcuts import render
from .models import Student
from api.models import Student
from .serializers import Studentserializer
from rest_framework.generics import ListAPIView
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.filter()
    serializer_class = Studentserializer

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby='Prachi')

