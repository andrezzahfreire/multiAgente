import re
import pandas as pd
from sentence_transformers import SentenceTransformer
import hnswlib

# Leitura do texto de entrada
with open("papeisAvulsos.txt", encoding="latin1") as f:
    texto = f.read()

# Inicializa modelo de embeddings
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Função para dividir o texto em blocos de tamanho fixo (em palavras)
def dividir_em_blocos(texto, tamanho=800):
    palavras = texto.split()
    return [" ".join(palavras[i:i+tamanho]) for i in range(0, len(palavras), tamanho)]

# Divide o texto em blocos
blocos = dividir_em_blocos(texto)
blocos = [b for b in blocos if len(b) > 100]  # remove blocos muito curtos

# Gera os embeddings
embeddings = modelo.encode(blocos, convert_to_numpy=True)

# Indexa os embeddings com hnswlib
index = hnswlib.Index(space="cosine", dim=384)
index.init_index(max_elements=len(blocos), ef_construction=200, M=16)
index.add_items(embeddings)

# Salva o índice e os blocos
index.save_index("indice.bin")
pd.DataFrame({"bloco": blocos}).to_csv("blocos.csv", index=False)

print("Indexação finalizada com sucesso.")
print(f"Número de blocos: {len(blocos)}")
