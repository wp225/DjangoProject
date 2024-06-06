# urls.py
from django.urls import path
from .views import home_view, next_view,success

urlpatterns = [
    path('', home_view, name='home_view'),
    path('next_view/', next_view, name='next_view'),
    path('success/',success,name="success")
]

