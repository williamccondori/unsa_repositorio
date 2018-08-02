from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from django.views.generic import View
from repositorio.models import Autor
from django.shortcuts import render


class AuthorListView(ListView):
    model = Autor
    template_name = 'author/list.html'


class AuthorDetailView(DetailView):
    model = Autor
    template_name = 'author/detail.html'


class AuthorCreate(View):
    TEMPLATE_NAME = 'author/create.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.TEMPLATE_NAME)


class AuthorUpdate(UpdateView):
    TEMPLATE_NAME = 'author/update.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.TEMPLATE_NAME)


class AuthorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('author-list')
    template_name = 'author/delete.html'
