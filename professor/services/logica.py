# professor/services/logica.py

from professor.models import CriterioAtividade


def corrigir_por_criterios(entrega):

    criterios = entrega.atividade.criterios.all()

    texto = entrega.resposta.lower()

    nota = 0
    feedback = []

    for criterio in criterios:

        palavra = criterio.palavra_chave.lower()

        if palavra in texto:

            nota += float(criterio.peso)

            feedback.append(
                f"✓ Encontrado: {criterio.palavra_chave}"
            )

        else:

            feedback.append(
                f"✗ Não encontrado: {criterio.palavra_chave}"
            )

    return {
        'nota': nota,
        'feedback': "\n".join(feedback)
    }