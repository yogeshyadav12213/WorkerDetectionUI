from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('', views.landing_view, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # Main Dashboard URLs
    path('dashboard/overview/', views.overview_view, name='overview'),
    path('dashboard/camera-management/', views.camera_management_view, name='camera_management'),
    path('dashboard/zone-configuration/', views.zone_configuration_view, name='zone_configuration'),
    path('dashboard/reports/', views.reports_view, name='reports'),
    path('dashboard/data-archive/', views.data_archive_view, name='data_archive'),

    # Placeholder URLs
    path('dashboard/live-stream/', views.placeholder_view, name='live_stream'),
    path('dashboard/system-settings/', views.placeholder_view, name='system_settings'),
]
