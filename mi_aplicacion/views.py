from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Hola desde Django en VS Code!")


from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
