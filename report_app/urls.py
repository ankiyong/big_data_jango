from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('graphpage/',views.graphpage,name='graph'),
    path('chart/',views.chart,name='chart'),
    path('livingchart/',views.livingchart,name='livingchart'),
    path('safechart/',views.safechart,name='safechart'),
    path('societychart/',views.societychart,name='societychart'),
# /finalchart

    ]