from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='surveys'),
    path('<int:survey_id', views.survey, name='survey'),
]
