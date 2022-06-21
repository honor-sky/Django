from . import views
from django.urls import path

app_name="gangmini_hompy"


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.project, name='project'),
    path('', views.index, name='index'),
]