import json
from professor.services.gemini_services import GeminiService


def corrigir_com_ia(atividade, entrega):

    criterios = atividade.criterios.all()

    criterios_formatados = []

    for c in criterios:
        criterios_formatados.append({
            "nome": c.nome,
            "descricao": c.descricao,
            "peso": float(c.peso)
        })

    prompt = f"""
Você é um avaliador acadêmico.

ATIVIDADE:
Título: {atividade.titulo}
Descrição: {atividade.descricao}

CRITÉRIOS:
{json.dumps(criterios_formatados, ensure_ascii=False, indent=2)}

RESPOSTA DO ALUNO:
{entrega.resposta}

INSTRUÇÕES:
- Avalie cada critério separadamente
- Dê nota respeitando o peso
- Gere feedback pedagógico
- Não use apenas palavras-chave, avalie contexto

RETORNE SOMENTE JSON:

{{
  "criterios": [
    {{
      "nome": "",
      "nota": 0,
      "feedback": ""
    }}
  ],
  "nota_final": 0
}}
"""

    resposta = GeminiService().gerar(prompt)

    return resposta