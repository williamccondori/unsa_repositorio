# Se agrega archivo de rutas para la aplicacion repositorio.

from django.urls import path, include
from . import views
from repositorio.controllers.dashboard_controller import DashboardController
from repositorio.controllers.document_controller import DocumentListView, DocumentCreate, DocumentUpdate, DocumentDelete

urlpatterns = [
    path('api/', include('repositorio.urls_api')),
    path('login/', DashboardController.as_view(), name='login'),
    path('', DashboardController.as_view(), name='dashboard'),
    
    path('document/', DocumentListView.as_view(), name='document-list'),
    path('document/add/', DocumentCreate.as_view(), name='document-add'),
    path('document/<int:pk>/', DocumentUpdate.as_view(), name='document-update'),
    path('document/<int:pk>/delete/', DocumentDelete.as_view(), name='document-delete'),
]