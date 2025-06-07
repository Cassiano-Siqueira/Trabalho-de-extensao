from django.shortcuts import render, redirect
from .forms import ContatoForm
from django.contrib import messages

def home(request):
    return render(request, 'site.html');

def contato_view(request):
   # print("request", request.POST)
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect(request.path)  # Redireciona para evitar reenviar o formulário
    else:
        form = ContatoForm()

    return render(request, 'site.html', {'form': form})  # Certifique-se que este é o nome correto do template

