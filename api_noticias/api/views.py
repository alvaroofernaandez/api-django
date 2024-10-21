from django.shortcuts import render
from django.views import View

from .models import Noticia

class NoticiasView(View):

    def get(self, request, idNoticia):


