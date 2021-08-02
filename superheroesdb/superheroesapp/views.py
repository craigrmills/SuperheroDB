from typing import ContextManager
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroesapp/index.html', context)


def detail(request, superhero_id):
    one_hero = Superhero.objects.get(pk=superhero_id)
    context = {
        'one_hero': one_hero
    }
    return render(request, 'superheroesapp/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        prim_superpower = request.POST.get('prim_superpower')
        secon_superpower = request.POST.get('secon_superpower')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, prim_superpower=prim_superpower,
                                  secon_superpower=secon_superpower, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroesapp:index'))
    else:
        return render(request, 'superheroesapp/create.html')


def remove(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    superhero.delete()
    return redirect(reverse('superheroesapp:index'))
