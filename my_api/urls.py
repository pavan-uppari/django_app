from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_items),
    path('items/', views.add_item),
    path('items/<int:id>/', views.get_item),
    # path('items/<int:id>/', views.update_item),
]