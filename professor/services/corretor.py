# professor/services/corretor.py

from .logica import corrigir_por_criterios


def corrigir_entrega(entrega):

    resultado = corrigir_por_criterios(
        entrega
    )

    entrega.nota = resultado['nota']

    entrega.feedback = resultado['feedback']

    entrega.corrigida = True

    entrega.save()

    return entrega