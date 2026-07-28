from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('create/', views.ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_edit'),
    path('<int:pk>/delete/', views.item_delete, name='item_delete'),
]