from django.contrib import admin
from .models import Cliente, Produtos, Telefone, CPF
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Telefone)
admin.site.register(Produtos)
admin.site.register(CPF)
