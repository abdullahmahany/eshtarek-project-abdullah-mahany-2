from django.urls import path
from .views import plans_list

urlpatterns = [
    path('plans/', plans_list),
]
