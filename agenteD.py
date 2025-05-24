from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def agenteD_resumir(texto: str) -> str:
    if len(texto) > 1000:
        texto = texto[:1000]
    resumo = summarizer(texto, max_length=100, min_length=30, do_sample=False)
    return resumo[0]['summary_text']