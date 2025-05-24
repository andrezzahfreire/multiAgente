from sentence_transformers import SentenceTransformer
import hnswlib
import pandas as pd

# Carregamento de modelo e índice
modelo = SentenceTransformer("all-MiniLM-L6-v2")
index = hnswlib.Index(space="cosine", dim=384)
index.load_index("indice.bin")
df = pd.read_csv("blocos.csv")

def agenteA_buscar(pergunta: str, limite_similaridade: float = 0.6, k: int = 7) -> str:
  
    emb = modelo.encode([pergunta], convert_to_numpy=True)
    total_blocos = index.get_current_count()
    if total_blocos == 0:
        return "Nenhum bloco encontrado. Reexecute o indexador com conteúdo válido."

    k = min(k, total_blocos)
    idxs, distances = index.knn_query(emb, k=k)

    resultados = []
    for i, d in zip(idxs[0], distances[0]):
        if d < limite_similaridade:
            bloco = df.iloc[i].bloco.strip()
            if bloco:  # evita blocos vazios
                resultados.append(bloco)

    if not resultados:
        return "Nenhum bloco relevante encontrado com base na similaridade."

    return "\n---\n".join(resultados)
