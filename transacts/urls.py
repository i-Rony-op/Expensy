from django.urls import path, include

from . import views

urlpatterns = [path("add_transac", views.add_transac, name="add_transac")]
