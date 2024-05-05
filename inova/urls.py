from django.urls import path
from inova.views import contato, home, sobre

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]
