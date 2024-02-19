from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def aluno (request):
    if request =='GET':
        aluno = {'id':'1', 'nome': 'everton'}
        return JsonResponse(aluno)
