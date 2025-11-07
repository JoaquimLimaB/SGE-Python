from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True, adicona a data de cadastro auyomatico, o dia de cadastro.
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True, toda vez que altera o produto altera a dat apara a atual de alteração.

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 