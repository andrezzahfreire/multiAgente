def agenteC_avaliar(resposta: str) -> str:
    if len(resposta.split()) < 4:
        return "Resposta curta demais. Reavalie."
    if any(p in resposta.lower() for p in ["não sei", "desconhecido", "irrelevante"]):
        return "Resposta vaga. Solicite nova tentativa."
    return "Resposta satisfatória."