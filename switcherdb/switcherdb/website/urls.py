from django.urls import path
from . import views

#routes for the urls
#example: yourURL/billing/ would execute views.inputBilling
urlpatterns = [
    path('', views.home, name="home"),
    path('join', views.join, name="join"),
    path('billing', views.inputBilling, name="billing"),
]