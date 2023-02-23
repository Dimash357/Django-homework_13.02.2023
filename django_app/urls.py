from django.urls import path
from . import views

app_name = 'django_app'
urlpatterns = [
    path('process-video/', views.process_video_view, name='process_video'),
]