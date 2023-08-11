from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dish_read, name="zomatoapp"),
    path("dish_add/", views.dish_add, name="dish_add"),
    path("dish_edit/<int:dish_id>/", views.dish_edit, name="dish_edit"),
    path("dish_delete/<int:dish_id>/", views.dish_delete, name="dish_delete"),
    path("dish_search/<int:dish_id>/", views.dish_search, name="dish_search"),
    path("orders/", views.orders, name="orders"),
    path("update_order_status/<int:order_id>/", views.update_order_status, name="update_order_status"),
    path("place_order/<int:dish_id>/", views.place_order, name="place_order"),
  
]