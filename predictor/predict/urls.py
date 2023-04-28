from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("test/" , views.testing , name="test"),
     path("submit/",views.user_forms_view , name = "submit")
 ]