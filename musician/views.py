from django.shortcuts import render, redirect
from . import forms
from . import models

def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_artist.html', {'form': musician_form})

def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = forms.MusicianForm(instance=musician)
    return render(request, 'add_artist.html', {'form': musician_form})