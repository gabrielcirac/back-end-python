from django.http import HttpResponse


from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={'name': 'Prof. Gabriel'})

def my_view(request):
    return HttpResponse("Uma teste string de resposta")

def user_view(request, username):
    return HttpResponse(f"Perfil do usuário: {username}")

def root_view(request):
    return HttpResponse("Estamos na Raiz 2. Porta 8000")



