from django.urls import path

from .views import blog_entries, entry_detail

app_name = 'blog'
urlpatterns = [
    path('entries/', blog_entries, name='blog_entries'),
    path('entries/<slug>/', entry_detail, name='entry_detail'),
]
