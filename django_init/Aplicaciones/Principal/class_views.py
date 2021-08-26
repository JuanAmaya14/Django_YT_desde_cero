from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView,DeleteView,ListView,UpdateView
from .forms import PersonaForm
from .models import Persona