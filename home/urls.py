from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('story/', views.story, name='story'),
    path('about/', views.about, name='about'),
    path('three-demo/', views.three_demo, name='three_demo'),  # 🔥 Added this
]
