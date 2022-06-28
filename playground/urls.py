from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.say_hello, name='store-home'),
    path('about/', views.about, name='store-about')
]
