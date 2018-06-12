from django.urls import path

from contact.views import contact_display

app_name = 'contact'
urlpatterns = [
    path('', contact_display, name='contact_display')
]
