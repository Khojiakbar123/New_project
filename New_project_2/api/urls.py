from django.urls import path
from api.views import index, detail

urlpatterns = [
    path('index/', index, name='index'),
    path('books/<int:pk>/', detail, name='detail'),
]
