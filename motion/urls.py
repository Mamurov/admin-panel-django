from django.urls import path
from django.contrib import admin
from .views import *

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('', index, name='home')
]
