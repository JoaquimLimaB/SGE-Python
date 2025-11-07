from django.db import models
from suppliers.models import Supplier
from products.models import Product


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True, adicona a data de cadastro auyomatico, o dia de cadastro.
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True, toda vez que altera o produto altera a dat apara a atual de alteração.

    class Meta:
        ordering = ['-created_at'] #(-)Coloca das datas mais recentes ate as mais antigas 

    def __str__(self):
        return str(self.product)
    