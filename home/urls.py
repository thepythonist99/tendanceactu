from django.urls import path

from home.views import home_display, event_display

app_name = 'home'
urlpatterns = [
    path('', home_display, name='home_display'),
    path('event/<slug>/', event_display, name='event_display'),
]
