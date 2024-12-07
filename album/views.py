from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models
from . import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView

@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    success_url = reverse_lazy('homepage')
    template_name = 'add_album.html'