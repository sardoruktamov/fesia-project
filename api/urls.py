from django.urls import path
from .views import CategoryListView, TeacherListCreateView

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("teachers/", TeacherListCreateView.as_view()),
]
