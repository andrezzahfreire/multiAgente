from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def agenteB_responder(pergunta: str, contexto: str, score_threshold=0.4) -> str:
    resultado = qa_pipeline(question=pergunta, context=contexto)
    if resultado['score'] < score_threshold or not resultado['answer'].strip():
        return "Não consegui encontrar uma resposta satisfatória no texto fornecido."
    return resultado['answer']