from django.urls import path
from django.contrib import admin
from .import views

urlpatterns=[
path('admin/', admin.site.urls),
path('create_view/',views.create_view),
path('upload_file/',views.upload_file),
path('update_view/<str:pk>/', views.update_view),
]