from django.contrib import admin
from .models import (
    Atividade,
    CriterioAtividade,
    EntregaAtividade
)

admin.site.register(Atividade)
admin.site.register(CriterioAtividade)
admin.site.register(EntregaAtividade)