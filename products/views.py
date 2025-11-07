from rest_framework import generics
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from app import metrics
from . import models, forms, serializers
from categories.models import Category
from brands.models import Brand
from django.contrib import messages 
from django.db.models.deletion import ProtectedError 
from django.shortcuts import render, redirect


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self): #Filtros 
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if category:
            queryset = queryset.filter(category__id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        return queryset
    
    def get_context_data(self, **kwargs):  # Sobrescrevendo o 'context_object_name'
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_product_metrics # Imporatnado as metricas de home(app)
        context['categories'] = Category.objects.all
        context['brands'] = Brand.objects.all
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'

                   # --- A LÓGICA PARA TRATAR O ERRO VEM AQUI ---
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
                f"O produto '{self.object}' não pode ser excluída, pois existem algo vinculado a ela."
            )
            # Redireciona o usuário de volta para a lista de categorias
            return redirect(self.success_url)
        
class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer