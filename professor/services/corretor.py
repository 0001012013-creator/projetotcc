import json
import re
from professor.services.gemini_services import GeminiService


def corrigir_com_ia(entrega):

    atividade = entrega.atividade
    criterios = atividade.criterios.all()

    criterios_formatados = []

    for c in criterios:
        criterios_formatados.append({
            "nome": c.nome,
            "descricao": c.descricao,
            "peso": float(c.peso)
        })

    prompt = f"""
Você é um avaliador acadêmico rigoroso.

ATIVIDADE:
Título: {atividade.titulo}
Descrição: {atividade.descricao}

CRITÉRIOS DE AVALIAÇÃO:
{json.dumps(criterios_formatados, ensure_ascii=False, indent=2)}

RESPOSTA DO ALUNO:
{entrega.resposta}

INSTRUÇÕES IMPORTANTES:
- Avalie CADA critério separadamente
- Considere o peso de cada critério
- Dê nota de 0 até o peso de cada critério
- Some para gerar a nota final
- Seja pedagógico no feedback

RETORNE APENAS UM JSON VÁLIDO.

REGRAS OBRIGATÓRIAS:
- Não escreva explicações
- Não use markdown
- Não use ``` ou ```json
- Não adicione texto antes ou depois
- A resposta deve começar com {{ e terminar com }}

FORMATO EXATO:

{{
  "criterios": [
    {{
      "nome": "nome do criterio",
      "nota": 0,
      "feedback": "comentário pedagógico"
    }}
  ],
  "nota_final": 0,
  "feedback_geral": "comentário geral sobre a resposta"
}}
"""

    try:
        resposta_ia = GeminiService().gerar(prompt)

        texto = resposta_ia

        # remove markdown
        texto = texto.replace("```json", "").replace("```", "").strip()

        # pega apenas o primeiro JSON válido completo
        match = re.search(r"\{[\s\S]*\}", texto)

        if match:
            json_limpo = match.group(0)
            resultado = json.loads(json_limpo)
        else:
            raise ValueError("JSON não encontrado")

    except Exception as e:

        print("\nERRO IA:")
        print(str(e))

        print("\nRESPOSTA IA:")
        try:
            print(texto)
        except:
            pass

        resultado = {
            "nota_final": 0,
            "feedback_geral": f"Erro ao interpretar resposta da IA: {str(e)}",
            "criterios": []
        }

    # salva no banco
    entrega.nota = resultado.get("nota_final", 0)
    entrega.feedback = resultado.get(
    "feedback_geral",
    ""
)
    entrega.corrigida = True
    entrega.save()

    return entrega

