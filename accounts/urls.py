from django.urls import path
from .views import *


urlpatterns = [
    path('', CustomerList.as_view() , name="home"),
    path('create/', CustomerCreate.as_view()),
   

   
    path('update/<int:pk>',Customerupdate.as_view(), name="update_order"),
    path('delete/<pk>',Customerdelete.as_view(), name="no_order"),


]