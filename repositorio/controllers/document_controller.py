from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from repositorio.models import Documento

class DocumentListView(ListView):
    model = Documento
    template_name = 'document/list.html'

class DocumentCreate(CreateView):
    model = Documento
    fields = ['titulo']
    template_name = 'document/create.html'


class DocumentUpdate(UpdateView):
    model = Documento
    fields = ['titulo']
    template_name = 'document/update.html'

class DocumentDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('document-list')
    template_name = 'document/delete.html'