from .views import plagiarismCheck, pricing, home
from django.urls import path, include

urlpatterns = [
    path('', home),
    path('pricing/', pricing),
    path('checkPlag/', plagiarismCheck),
]