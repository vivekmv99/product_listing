from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('pro_list/<int:pk>',views.pro_list,name="pro_list"),
]