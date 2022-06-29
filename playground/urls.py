from django.urls import URLPattern, path
from . import views

# for server routing
urlpatterns = [
    path('', views.say_hello, name='store-home'),
    path('about/', views.about, name='store-about')
]
