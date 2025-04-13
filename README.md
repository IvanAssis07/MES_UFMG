# Comparação de LLMs na Resolução de Desafios de Programação usados em Recrutamento

## Grupo formado por:
Henrique da Fonseca Diniz Freitas (2021031688)

Ivan Vilaça de Assis (2021421931)

Marcelo Augusto Mrad Marteleto (2021031548)


## Objetivo

Este estudo tem como objetivo **avaliar o desempenho de diferentes modelos de linguagem de última geração** (LLMs - Large Language Models) na **resolução de desafios de programação**, utilizando problemas populares da plataforma LeetCode. O foco está em analisar a capacidade dos modelos em diferentes níveis de dificuldade e em mais de uma linguagem de programação.

Além de comparar modelos amplamente discutidos na literatura, como o **GPT-4o**, este trabalho também busca lançar luz sobre modelos emergentes como o **Claude** (Anthropic) e o **DeepSeek-Coder**, cuja atuação prática ainda é pouco explorada academicamente.

---

## Metodologia

### Modelos de Linguagem Utilizados

- **GPT-4o** (OpenAI)
- **Claude** (Anthropic)
- **DeepSeek-Coder** (DeepSeek)

> Critério de escolha: Popularidade, disponibilidade de acesso e **ausência de estudos comparativos aprofundados** em ambientes de codificação desafiadora, como o LeetCode.

---

### Dataset

- **Fonte**: LeetCode
- **Seleção**: Top 100 problemas mais populares da plataforma
- **Distribuição**:
  - 15 problemas fáceis
  - 15 problemas médios
  - 15 problemas difíceis

> Critério de seleção: Popularidade (ranking do próprio LeetCode), abrangência de estruturas de dados e algoritmos, e variedade de temas.

---

### Prompting

- **Formato dos Prompts**:
  - Cada prompt contém **apenas o enunciado original** da questão no LeetCode e a **linguagem de programação desejada**.
  - Nenhuma instrução adicional será fornecida (zero-shot).
  
- **Linguagens utilizadas**:
  - **Python**
  - **C**

- Cada problema será testado **com 3 execuções distintas** por modelo (para considerar variação na geração).
- Será considerada **a melhor resposta entre as três**.

---

### Avaliação Quantitativa

- **Critério principal**: Avaliação automática via LeetCode (ou simulador compatível)
- **Métrica de desempenho**:
  - **Aceitação total**: Passou todos os testes
  - **Aceitação parcial**: Passou pelo menos 50% dos testes
  - **Rejeição**: Falhou mais de 50% dos testes
  
- Para cada modelo será registrada:
  - **Taxa de acerto total (%)**
  - **Distribuição de desempenho por nível de dificuldade**
  - **Desempenho por linguagem (Python x C)**

---

### Avaliação Qualitativa

- Para cada nível de dificuldade, serão selecionados **3 exemplos por modelo** para análise manual.
- Os critérios analisados serão:
  - Clareza e estrutura do código gerado
  - Uso apropriado de algoritmos e estruturas de dados
  - Legibilidade e comentários (se houver)
  - Robustez e tratamento de casos extremos
