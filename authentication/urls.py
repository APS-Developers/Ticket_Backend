from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('update/<str:pk>/', views.updateUser, name='update'),
    path('delete/<str:pk>/', views.deleteUser, name='delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),   # submit email form
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),   # email sent success message
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),  # link to password reset form in mail
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),   # password successfully changed message

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
