from django.urls import path
from .views import HomePagesViews


urlpatterns = [
    path('home/',HomePagesViews.as_view(), name='home')
]