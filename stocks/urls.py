from . import views
from django.urls import path
#from .views import home, stock_detail, stock_create, stock_edit, stock_delete

urlpatterns = [
    path('', views.home, name='home'),
    path('stock/<int:pk>/', views.stock_detail, name='stock_detail'),
    path('stock/new/', views.stock_create, name='stock_create'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
]