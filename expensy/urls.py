from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("accounts/", include("accounts.urls")),
    path("transacts/", include("transacts.urls")),
    # path("result", views.result, name="result"),
]
