from django.urls import path

from escola.views import aluno


urlpatterns = [
    path('',aluno),
    path('escola/', aluno)

]