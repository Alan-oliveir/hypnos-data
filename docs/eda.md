# Análise Exploratória de Dados (EDA)

## Objetivos da Análise

A Análise Exploratória de Dados (EDA) tem como objetivo compreender a estrutura do dataset, identificar padrões, detectar anomalias e formular hipóteses sobre os fatores que influenciam a eficiência do sono.

## Estatísticas Descritivas

### Variáveis Quantitativas

As principais métricas estatísticas das variáveis numéricas revelam:

- **Idade:** Distribuição ampla, média de 40 anos
- **Duração do Sono:** Média de 7 horas, com variação de 5 a 9 horas
- **Eficiência do Sono:** Distribuição concentrada entre 0.7 e 0.9
- **Despertares:** Média de aproximadamente 1-2 por noite
- **Consumo de Cafeína:** Variação significativa entre participantes
- **Consumo de Álcool:** Maioria com consumo baixo ou nulo

### Variáveis Qualitativas

**Distribuição por Gênero:**
- Leve predominância do gênero masculino
- Distribuição relativamente equilibrada

**Status de Fumante:**
- Maioria não fumante
- Pequena proporção de fumantes ativos

**Frequência de Exercícios:**
- Distribuição bimodal: picos em 0 dias/semana e 3 dias/semana
- Variação ampla entre participantes

## Análise Bivariada

Foram testadas **12 hipóteses** para investigar relações entre a eficiência do sono e diversos fatores.

### Hipóteses sobre Eficiência do Sono

#### Hipótese 1: Eficiência do Sono vs. Idade

**Correlação de Pearson:** Fraca correlação negativa

**Interpretação:** A idade tem impacto limitado na eficiência do sono. Embora haja uma leve tendência de redução com o aumento da idade, outros fatores são mais determinantes.

#### Hipótese 2: Eficiência do Sono vs. Status de Fumante

**Resultado:**
- Não fumantes: Eficiência ligeiramente superior
- Fumantes: Eficiência ligeiramente inferior

**Interpretação:** O tabagismo mostra algum impacto negativo, mas não é o fator mais determinante.

#### Hipótese 3: Eficiência do Sono vs. Frequência de Exercícios

**Resultado:** Relação positiva clara

**Correlação:** +0.26 (positiva moderada)

**Interpretação:** A prática regular de exercícios físicos está associada a melhor eficiência do sono. Este é um dos **fatores positivos mais importantes** identificados.

### Qualidade do Sono e Exercícios Físicos

#### Hipótese 4: Sono Leve vs. Frequência de Exercícios

**Resultado:** Pessoas que se exercitam regularmente tendem a ter menor percentual de sono leve.

#### Hipótese 5: Sono REM vs. Frequência de Exercícios

**Resultado:** Exercícios regulares estão associados a maiores percentuais de sono REM.

#### Hipótese 6: Sono Profundo vs. Frequência de Exercícios

**Resultado:** Exercícios físicos favorecem o aumento do sono profundo, essencial para recuperação física.

!!! success "Conclusão - Exercícios"
    A prática regular de exercícios físicos melhora não apenas a eficiência total do sono, mas também favorece estágios mais reparadores (REM e profundo) em detrimento do sono leve.

### Qualidade do Sono e Consumo de Álcool

#### Hipótese 7: Sono Leve vs. Consumo de Álcool

**Resultado:** Maior consumo de álcool está associado a maior percentual de sono leve.

#### Hipótese 8: Sono REM vs. Consumo de Álcool

**Resultado:** O álcool reduz significativamente o sono REM, prejudicando a qualidade.

#### Hipótese 9: Sono Profundo vs. Consumo de Álcool

**Resultado:** O consumo de álcool também reduz o sono profundo.

!!! danger "Conclusão - Álcool"
    O consumo de álcool tem um impacto **fortemente negativo** na qualidade do sono, reduzindo os estágios reparadores (REM e profundo) e aumentando o sono leve. Correlação: -0.38

### Qualidade do Sono e Consumo de Cafeína

#### Hipótese 10: Sono Leve vs. Consumo de Cafeína

**Resultado:** Consumo elevado de cafeína está associado a maior percentual de sono leve.

#### Hipótese 11: Sono REM vs. Consumo de Cafeína

**Resultado:** A cafeína tende a reduzir o sono REM.

#### Hipótese 12: Sono Profundo vs. Consumo de Cafeína

**Resultado:** O consumo de cafeína nas 24 horas anteriores prejudica o sono profundo.

!!! warning "Conclusão - Cafeína"
    Embora com impacto menor que o álcool, o consumo de cafeína (especialmente próximo ao horário de dormir) prejudica os estágios profundos do sono.

## Análise Multivariada

### Matriz de Correlação

A análise de correlação entre todas as variáveis numéricas revela:

**Correlações Mais Fortes com Sleep Efficiency:**

| Variável | Correlação | Interpretação |
|----------|-----------|---------------|
| **Awakenings** | **-0.55** | Forte impacto negativo |
| **Alcohol consumption** | **-0.38** | Impacto negativo moderado |
| **Exercise frequency** | **+0.26** | Impacto positivo moderado |
| **Caffeine consumption** | -0.15 | Impacto negativo leve |
| **Age** | -0.10 | Impacto muito fraco |
| **Sleep duration** | +0.08 | Praticamente independente |

### Insights da Correlação

!!! info "Descoberta Importante"
    **Duração vs. Qualidade:** A duração do sono tem correlação quase nula com a eficiência (+0.08). Isso significa que **dormir por mais tempo não garante melhor qualidade de sono**.

!!! danger "Maior Vilão"
    Os **despertares noturnos** são o fator que mais prejudica a eficiência do sono (correlação de -0.55), seguidos pelo consumo de álcool (-0.38).

!!! success "Maior Aliado"
    A **frequência de exercícios** é o principal fator benéfico identificado (+0.26), seguido pela ausência de consumo de álcool e cafeína.

## Principais Conclusões da EDA

### Padrões Identificados

1. **Exercício Físico Regular:** Melhora significativa na eficiência e qualidade do sono
2. **Consumo de Álcool:** Forte impacto negativo, especialmente em estágios REM e profundo
3. **Despertares Noturnos:** Principal fator prejudicial à eficiência
4. **Duração ≠ Qualidade:** Tempo de sono não garante eficiência

### Tratamento de Dados

- **Valores Faltantes:** Identificados e tratados com imputação pela mediana
- **Outliers:** Detectados, mas mantidos para análise (podem representar casos reais de distúrbios do sono)
- **Conversão de Tipos:** Datas e horários convertidos para formato apropriado

### Implicações para Modelagem

Os insights da EDA guiam as próximas etapas:

- **Features mais relevantes:** Awakenings, Alcohol consumption, Exercise frequency
- **Necessidade de normalização:** Variáveis em escalas diferentes
- **Encoding de categóricas:** Gender, Smoking status
- **Engenharia de features:** Transformação de horários em componentes cíclicos

## Próximos Passos

Com os padrões identificados, avançamos para:

- [Pré-processamento](preprocessing.md) - Preparação dos dados para modelagem
- [Modelagem](modeling.md) - Aplicação de algoritmos de Machine Learning
- [Resultados](results.md) - Análise final e conclusões
