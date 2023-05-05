from django.urls import path
from .views import home, add_student, delete_student

urlpatterns = [
    path('', home, name='home'),
    path('add_student/', add_student, name='add_student'),
    path('delete_student/<int:pk>/', delete_student, name='delete_student'),
]
