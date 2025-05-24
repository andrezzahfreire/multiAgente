# Sistema Multiagente para Análise Textual da Obra *O Alienista*, de Machado de Assis

---

## 1. Descrição do sistema multiagente implementado

O sistema é composto por quatro agentes que atuam de forma coordenada para analisar o texto da obra *O Alienista*, de Machado de Assis, e responder perguntas feitas pelo usuário. A arquitetura é organizada da seguinte forma:

- **Agente A (ContextRetriever):** Recupera blocos relevantes do texto com base na pergunta do usuário.  
- **Agente D (Resumo):** Recebe os blocos recuperados e realiza um resumo para reduzir redundância e focar nos pontos essenciais.  
- **Agente B (AnswerGenerator):** Gera a resposta textual a partir do resumo fornecido pelo Agente D.  
- **Agente C (AnswerEvaluator):** Avalia a qualidade da resposta gerada e indica se está satisfatória ou se precisa ser refeita.

Este fluxo visa otimizar a compreensão do conteúdo, melhorando a eficiência da geração das respostas e possibilitando a observação do impacto da compressão semântica do resumo na qualidade final.

---

## 2. Função e utilidade do Agente D (Resumidor)

O Agente D tem como função principal transformar os blocos textuais extensos e potencialmente redundantes, fornecidos pelo Agente A, em resumos mais concisos e focados, facilitando o processamento e a geração das respostas pelo Agente B. A utilidade do Agente D está em:

- Reduzir o volume de texto a ser processado, otimizando o uso dos modelos de linguagem.  
- Eliminar informações irrelevantes ou repetidas, potencialmente melhorando a clareza da resposta final.  
- Permitir o estudo do impacto da compressão semântica na precisão e adequação das respostas.

---

## 3. Execuções e resultados

### Execução 1  
**Pergunta:** “Por que o personagem Simão Bacamarte decide internar a esposa no hospício?”  

- [AgenteA - ContextRetriever]: Contexto recuperado com 34386 caracteres  
- [Agente D - Resumo]:  
  "a camara a cassar a licena, vel-o-hia na rua e restituido ao logar . o barbeiro porfirio recorreram secretamente afianaram-lhe todo, o apoio de gente, dinheiro e influencia, se elle se puzesse"  
- [AgenteB - AnswerGenerator]:  
  "Não consegui encontrar uma resposta satisfatória no texto fornecido."  
- [AgenteC - AnswerEvaluator]:  
  "Resposta satisfatória."  

**Comentário:**  
O resumo gerado foi truncado e pouco coerente, resultando na incapacidade do sistema em gerar uma resposta adequada. Isso mostra que a compressão semântica, neste caso, prejudicou a qualidade da resposta, indicando necessidade de melhorias no agente de resumo.

---

### Execução 2  
**Pergunta:** “Qual é a reação da população de Itaguaí às ações do Dr. Bacamarte ao longo da história?”  

- [AgenteA - ContextRetriever]: Contexto recuperado com 34359 caracteres  
- [Agente D - Resumo]:  
  "o pae do Nicolu, adquirindo o despacho de capit£o, corrigia esse ponto da anatomia gentilica foi tambem levar a sua pedra ao caes ."  
- [AgenteB - AnswerGenerator]:  
  "Não consegui encontrar uma resposta satisfatória no texto fornecido."  
- [AgenteC - AnswerEvaluator]:  
  "Resposta satisfatória."  

**Comentário:**  
O resumo apresentou fragmentos desconexos e caracteres estranhos, o que comprometeu a geração de uma resposta útil. Isso evidencia que o processo de resumo precisa ser ajustado para melhor preservar o sentido do conteúdo.

---

### Execução 3  
**Pergunta:** “Qual o papel do barbeiro Porfírio na trama e como ele influencia os acontecimentos?”  

- [AgenteA - ContextRetriever]: Contexto recuperado com 34270 caracteres  
- [Agente D - Resumo]:  
  "o pae do Nicolu, adquirindo o despacho de capit£o, corrigia esse ponto da anatomia gentilica foi tambem levar a sua pedra ao caes ."  
- [AgenteB - AnswerGenerator]:  
  "Não consegui encontrar uma resposta satisfatória no texto fornecido."  
- [AgenteC - AnswerEvaluator]:  
  "Resposta satisfatória."  

**Comentário:**  
Mais uma vez, o resumo pouco inteligível comprometeu a resposta. O impacto do resumo mal estruturado é visível na baixa pertinência das respostas geradas, sinalizando que o agente resumidor deve ser melhor calibrado.

---

## 4. Considerações finais

O sistema multiagente implementado conseguiu orquestrar as etapas de recuperação, resumo, geração e avaliação das respostas. Entretanto, o agente de resumo demonstrou dificuldades ao lidar com o volume e qualidade do texto, afetando negativamente a resposta final. Recomenda-se aprimorar o pré-processamento e os parâmetros do modelo de resumo para garantir resumos coesos e representativos, melhorando a eficácia do sistema.
