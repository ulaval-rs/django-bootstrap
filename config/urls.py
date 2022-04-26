from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("apps.rest.v1.urls")),
    path("admin/", admin.site.urls),
]
