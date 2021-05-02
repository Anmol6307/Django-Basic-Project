from django.urls import path
from . import views

urlpatterns = [
    path('feesdj/', views.Fees_Django),
]