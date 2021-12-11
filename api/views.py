from rest_framework import generics
from .serializers import CategorySerializer, TeacherSerializer
from .models import Categories, Teacher, Course, Video, Task, Homework

# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


#GET and POST
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer