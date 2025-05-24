from agenteA import agenteA_buscar
from agenteB import agenteB_responder
from agenteC import agenteC_avaliar
from agenteD import agenteD_resumir

def executar_fluxo(pergunta):
    
    print(f"[Usuário]: {pergunta}")
    
    contexto = agenteA_buscar(pergunta)
    print(f"[AgenteA - ContextRetriever]: Contexto recuperado com {len(contexto)} caracteres")
    
    resumo = agenteD_resumir(contexto)
    print(f"[Agente D - Resumo]: {resumo}\n")

    resposta = agenteB_responder(pergunta, contexto=resumo)
    print(f"[AgenteB - AnswerGenerator]: {resposta}")

    avaliacao = agenteC_avaliar(resposta)
    print(f"[AgenteC - AnswerEvaluator]: {avaliacao}")

if __name__ == "__main__":
    executar_fluxo("Por que o personagem Simão Bacamarte decide internar a esposa no hospício?")
    executar_fluxo("Qual é a reação da população de Itaguaí às ações do Dr. Bacamarte ao longo da história?")
    executar_fluxo("Qual o papel do barbeiro Porfírio na trama e como ele influencia os acontecimentos?")
    
    