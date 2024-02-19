from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

def aluno (request):
    return HttpResponse('<h1>espaço pessoal</h1><p>apenas testando codigo</p>')


