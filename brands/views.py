from rest_framework import generics
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models, forms 
from django.contrib import messages 
from django.db.models.deletion import ProtectedError 
from django.shortcuts import render, redirect
from . import serializers


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10
    permission_required = 'brands.view_brand'  # Permição de usuario:  Formato 'nomeDaApp.ação_nomeDoModel'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name: #Filtro
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')    
    permission_required = 'brands.add_brand' 


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand' 


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'brand_update.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.change_brand' 


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.delete_brand' 

            # --- A LÓGICA PARA TRATAR O ERRO ---
    def post(self, request, *args, **kwargs):
        # self.get_object() pega o objeto que está sendo deletado (neste caso, a categoria)
        self.object = self.get_object() 
        try:
            # Tenta executar a exclusão padrão da DeleteView
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            # Se o erro de proteção for acionado, executa este bloco
            messages.error(
                request,
                f"A marca'{self.object}' não pode ser excluída, pois existem produtos vinculados a ela."
            )
            # Redireciona o usuário de volta para a lista de categorias
            return redirect(self.success_url)

class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

