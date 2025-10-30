# Dataset: Sleep Efficiency

## Fonte dos Dados

O conjunto de dados utilizado neste projeto é o **Sleep Efficiency**, disponível publicamente no Kaggle.

**Fonte:** [Sleep Efficiency Dataset - Kaggle](https://www.kaggle.com/datasets/equilibriumm/sleep-efficiency)

**URL do Dataset:** `https://raw.githubusercontent.com/atlantico-academy/datasets/refs/heads/main/sleep_efficiency.csv`

## Visão Geral

O dataset contém informações sobre padrões de sono e fatores de estilo de vida de 452 participantes, com 15 variáveis que descrevem características demográficas, comportamentais e métricas relacionadas ao sono.

### Estatísticas Básicas

- **Total de Amostras:** 452 registros
- **Total de Variáveis:** 15
- **Período de Coleta:** Não especificado
- **Valores Faltantes:** Presentes em algumas variáveis (tratados durante o pré-processamento)

## Dicionário de Dados

### Variáveis Identificadoras

| Variável | Tipo | Descrição |
|----------|------|-----------|
| **ID** | Quantitativa Discreta | Identificação única do paciente |

### Variáveis Demográficas

| Variável | Tipo | Descrição |
|----------|------|-----------|
| **Age** | Quantitativa Discreta | Idade do paciente (anos) |
| **Gender** | Qualitativa Nominal | Gênero do paciente (Male/Female) |

### Variáveis Temporais

| Variável | Tipo | Descrição |
|----------|------|-----------|
| **Bedtime** | Qualitativa Ordinal | Hora que cada paciente vai para a cama |
| **Wakeup time** | Qualitativa Ordinal | Hora que cada paciente acorda |

### Métricas de Sono

| Variável | Tipo | Descrição |
|----------|------|-----------|
| **Sleep duration** | Quantitativa Contínua | Duração total do sono em horas |
| **Sleep efficiency** | Quantitativa Contínua | Proporção do tempo na cama que foi realmente gasto dormindo (0-1) ⭐ **Variável Alvo** |
| **REM sleep percentage** | Quantitativa Discreta | Percentual de tempo gasto em sono REM |
| **Deep sleep percentage** | Quantitativa Discreta | Percentual de tempo gasto em sono profundo |
| **Light sleep percentage** | Quantitativa Discreta | Percentual de tempo gasto em sono leve |
| **Awakenings** | Quantitativa Discreta | Número de vezes que o indivíduo acorda durante a noite |

### Fatores de Estilo de Vida

| Variável | Tipo | Descrição |
|----------|------|-----------|
| **Caffeine consumption** | Quantitativa Discreta | Consumo de cafeína nas 24 horas anteriores (mg) |
| **Alcohol consumption** | Quantitativa Discreta | Consumo de álcool nas 24 horas anteriores (doses) |
| **Smoking status** | Qualitativa Nominal | Status de fumante (Yes/No) |
| **Exercise frequency** | Qualitativa Ordinal | Frequência de exercícios por semana (dias) |

## Variável Alvo

A variável principal de análise e predição é a **Sleep efficiency** (Eficiência do Sono), que representa a proporção do tempo na cama que foi efetivamente gasto dormindo. 

**Fórmula:**
$$
\text{Sleep Efficiency} = \frac{\text{Tempo Real de Sono}}{\text{Tempo Total na Cama}}
$$

Valores próximos de 1.0 (ou 100%) indicam alta eficiência do sono.

## Classificação das Variáveis

### Por Tipo Estatístico

**Quantitativas Contínuas:**
- Sleep duration
- Sleep efficiency
- Awakenings

**Quantitativas Discretas:**
- ID
- Age
- REM Sleep percentage
- Deep sleep percentage
- Light sleep percentage
- Caffeine consumption
- Alcohol consumption

**Qualitativas Nominais:**
- Gender
- Smoking status

**Qualitativas Ordinais:**
- Bedtime
- Wakeup time
- Exercise frequency

## Observações Iniciais

!!! info "Características do Dataset"
    - **Distribuição de Gênero:** Leve predominância masculina
    - **Idade Média:** 40 anos
    - **Duração Média do Sono:** 7 horas
    - **Duração Mínima:** 5 horas
    - **Status de Fumante:** Maioria não fumante
    - **Exercício Físico:** Variação ampla, com picos em 0 e 3 dias por semana

!!! warning "Valores Faltantes"
    Algumas variáveis apresentam valores faltantes que foram tratados durante o pré-processamento:
    
    - Awakenings
    - Caffeine consumption
    - Alcohol consumption
    - Exercise frequency
    
    **Estratégia:** Imputação pela mediana (variáveis numéricas)

## Próximos Passos

Após compreender a estrutura do dataset, explore as análises realizadas:

- [Análise Exploratória de Dados](eda.md) - Visualizações e estatísticas descritivas
- [Pré-processamento](preprocessing.md) - Tratamento de dados e engenharia de features
- [Modelagem](modeling.md) - Algoritmos de Machine Learning aplicados
