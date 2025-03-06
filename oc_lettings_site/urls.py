"""Configuration des URLs de l'application principale."""

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-test/', lambda request: 1 / 0, name='sentry-test'),
]
