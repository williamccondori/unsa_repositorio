from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from repositorio.models import Autor

class AuthorListView(ListView):
    model = Autor
    template_name = 'author/list.html'

class AuthorDetailView(DetailView):
    model = Autor
    template_name = 'author/detail.html'

class AuthorCreate(CreateView):
    model = Autor
    fields = ['nombre']
    template_name = 'author/create.html'

class AuthorUpdate(UpdateView):
    model = Autor
    fields = ['nombre']
    template_name = 'author/update.html'

class AuthorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('author-list')
    template_name = 'author/delete.html'