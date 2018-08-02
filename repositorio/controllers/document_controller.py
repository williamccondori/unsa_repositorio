from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.views.generic import View
from django.shortcuts import render

from repositorio.models import Documento
from repositorio.models import Autor

# Services
from repositorio.services.document_service import DocumentService
# Dtos
from repositorio.dtos.document_dto import DocumentDto


class DocumentListView(View):
    TEMPLATE_NAME = 'document/list.html'

    def get(self, request, *args, **kwargs):
        documents = Documento.objects.all()
        return render(request, self.TEMPLATE_NAME, {'documents': documents})


class DocumentDetailView(DetailView):
    model = Documento
    template_name = 'document/detail.html'


class DocumentCreate(View):
    TEMPLATE_NAME = 'document/create.html'
    TEMPLATE_NAME_MESSAGE = 'document/message.html'

    def get(self, request, *args, **kwargs):
        authors = Autor.objects.all()
        return render(request, self.TEMPLATE_NAME, {'authors': authors})

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        author_id = request.POST['author_id']
        year = request.POST['year']
        summary = request.POST['summary']
        document_file = request.FILES['document_file']
        document_dto = DocumentDto(
            title=title,
            author_id=author_id, year=year, summary=summary, document_file=document_file)
        document_service = DocumentService()
        document_service.save(document_dto)
        return render(request, self.TEMPLATE_NAME_MESSAGE)


class DocumentUpdate(UpdateView):
    TEMPLATE_NAME = 'document/update.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.TEMPLATE_NAME)


class DocumentDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('document-list')
    template_name = 'document/delete.html'
