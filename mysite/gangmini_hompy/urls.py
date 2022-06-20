from . import views
from django.urls import path

app_name="gangmini_hompy"


urlpatterns = [
    path('', views.index, name='index'),
]