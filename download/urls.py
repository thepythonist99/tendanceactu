from django.urls import path

from download.views import download_display

app_name = 'download'
urlpatterns = [
    path('music/', download_display, name='download_display'),
]
