from django.urls import path
from rest.views import CarList

urlpatterns = [
    path('cars/', CarList.as_view(), name='index'),
    path('books/<int:pk>/', CarList.as_view()),
]
