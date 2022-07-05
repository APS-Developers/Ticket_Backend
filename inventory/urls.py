from django.urls import path
from django.contrib import admin
from django_filters.views import FilterView
from . import views

urlpatterns=[
path('admin/', admin.site.urls),
path('create_view/',views.create_view),
path('upload_file/',views.upload_file),
path('show/',views.showInventory),
path('update_view/<str:pk>/', views.update_view),
]