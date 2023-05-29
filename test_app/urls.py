from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test_app-home'),
    path('search_events/', views.search_events, name='test_app_search_events'),
    path('browse_events/', views.browse_events, name='test_app_browse_events'),
    path('event_info/', views.event_info, name='test_app_event_info'),
]