from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.Learn_Django),
]