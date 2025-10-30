# Análise da Eficiência do Sono

## Objetivo do Projeto

O objetivo deste projeto é analisar e identificar padrões e correlações entre a eficiência do sono e diversos fatores de estilo de vida. Tais informações podem oferecer insights valiosos sobre os principais aspectos que influenciam a qualidade do sono.

## Justificativa

A qualidade do sono é essencial para a saúde e o bem-estar físico, mental e emocional. Dormir mal pode afetar a **produtividade** e aumentar o risco de **doenças cardiovasculares, doenças metabólicas e distúrbios mentais.**

A análise da eficiência do sono, considerando fatores de estilo de vida, como rotinas e hábitos de consumo, pode contribuir para o desenvolvimento de estratégias que influenciem na melhoria da qualidade do sono e a saúde em geral.

## Resumo do Projeto

Este projeto de Data Science foi desenvolvido como trabalho final do curso e está estruturado em três etapas principais:

### 1. Análise Exploratória de Dados (EDA)
- Análise descritiva das variáveis
- Visualizações de distribuições
- Análise de correlações
- Testes de 12 hipóteses sobre fatores que afetam o sono

### 2. Pré-processamento e Engenharia de Features
- Tratamento de valores faltantes
- Transformação de variáveis temporais em features cíclicas
- Normalização e encoding de variáveis
- Pipeline automatizado de pré-processamento

### 3. Modelagem Preditiva
- Comparação de 7 algoritmos de Machine Learning
- Validação cruzada com K-Fold (30 folds)
- Otimização de hiperparâmetros
- Análise de métricas (R², MAE, MSE)

## Principais Descobertas
!!! success "Fatores Positivos"
    - **Exercícios Físicos**: Correlação positiva (+0.26) com eficiência do sono
    - Prática regular melhora significativamente a qualidade do sono

!!! danger "Fatores Negativos"
    - **Despertares Noturnos**: Forte correlação negativa (-0.55)
    - **Consumo de Álcool**: Correlação negativa (-0.38)
    - Ambos prejudicam significativamente a eficiência do sono

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Seaborn](https://img.shields.io/badge/seaborn-%2300A2C1.svg?style=for-the-badge&logo=seaborn&color=444876&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Scikit Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Equipe de Desenvolvimento

- [Alan de Oliveira Gonçalves](https://github.com/Alan-oliveir)
- Ayrton Lucas Viana Albuquerque Silva
- Cauan Halison Arantes de Oliveira
- Hosana Maria Ferro Dias

**Disciplina:** Ciência de Dados  
**Professor:** Madson Dias

---

## Navegação Rápida

<div class="grid cards" markdown>

-   :material-database:{ .lg .middle } __Dataset__

    ---

    Conheça o conjunto de dados Sleep Efficiency do Kaggle

    [:octicons-arrow-right-24: Explorar Dataset](dataset.md)

-   :material-chart-line:{ .lg .middle } __Análise Exploratória__

    ---

    Visualizações, estatísticas e insights dos dados

    [:octicons-arrow-right-24: Ver Análises](eda.md)

-   :material-brain:{ .lg .middle } __Modelagem__

    ---

    Comparação de algoritmos de Machine Learning

    [:octicons-arrow-right-24: Ver Modelos](modeling.md)

-   :material-trophy:{ .lg .middle } __Resultados__

    ---

    Conclusões e principais achados do projeto

    [:octicons-arrow-right-24: Ver Resultados](results.md)

</div>
