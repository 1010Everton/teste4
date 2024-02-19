from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

def aluno (request):
    return render(request,'index.html')


