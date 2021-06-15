from django.urls import path

from . import views

urlpatterns = [
    path('', views.fun, name="fun"),
    path('display/<data>/<size>', views.display, name="display"),
    

]
