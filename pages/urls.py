from django.urls import path
from .views import HomePagesViews


urlpatterns = [
    path('', HomePagesViews.as_view(), name='home'),
]
