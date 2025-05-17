from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import ProfessorForm
from .models import Professor

def home(request):
    return HttpResponse('estou na home')

def cadastro(request):
    formulario = ProfessorForm(request.POST or None)
    
    if formulario .is_valid():
        formulario.save()
        return HttpResponse('professor cadastrado!') 
    
    return render(request, 'cadastro.html', {'form':formulario})