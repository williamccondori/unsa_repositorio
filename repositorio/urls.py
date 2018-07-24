from django.urls import path, include
from . import views

from repositorio.controllers.document_controller import DocumentListView, DocumentDetailView, DocumentCreate, DocumentUpdate, DocumentDelete
from repositorio.controllers.author_controller import AuthorListView, AuthorDetailView, AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    path('api/', include('repositorio.urls_api')),
    
    path('', views.dashboard, name='dashboard'),
    path('manage', views.manage, name='manage'),

    # Document urls
    path('document/', DocumentListView.as_view(), name='document-list'),
    path('document/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('document/add/', DocumentCreate.as_view(), name='document-add'),
    path('document/<int:pk>/update/', DocumentUpdate.as_view(), name='document-update'),
    path('document/<int:pk>/delete/', DocumentDelete.as_view(), name='document-delete'),

    # Author urls
    path('author/', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('author/<int:pk>/update', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]