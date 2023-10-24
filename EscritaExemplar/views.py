from django.shortcuts import render,get_object_or_404,redirect
from .models import Usuario, Redacao
from .form import UsuarioForm, RedacaoForm
from django.views import View
from django.views.generic import ListView
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator, Page
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(View):
    template_name = "EscritaExemplar/index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('erro')
        return super().dispatch(request,*args, **kwargs)

    def get(self, request):
        return render(request, self.template_name)
