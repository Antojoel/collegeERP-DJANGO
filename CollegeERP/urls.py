from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
    # Fixed logout URL to accept GET requests
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='/', template_name='info/logout.html'), 
         name='logout'),
]