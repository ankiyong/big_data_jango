from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('graphpage/',views.graphpage,name='graph')
    ]