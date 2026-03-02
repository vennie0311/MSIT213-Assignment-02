from django.urls import path
from .views import DashboardView, AssetListView, MaintenanceCreateView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('asset/<int:pk>/maintain/', MaintenanceCreateView.as_view(), name='maintain_asset'),
]