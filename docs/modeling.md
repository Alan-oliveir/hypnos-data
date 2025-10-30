# Modelagem e Comparação de Algoritmos

## Objetivo

Comparar diferentes algoritmos de Machine Learning para predição da eficiência do sono, identificando qual modelo apresenta o melhor desempenho e maior capacidade de generalização.

## Método de Validação

### K-Fold Cross-Validation

Utilizamos **K-Fold Cross-Validation** com **30 folds** para avaliar os modelos de forma robusta.

#### Como Funciona

1. O dataset é dividido em 30 subconjuntos (folds) de tamanhos semelhantes
2. Em cada iteração:
   - 29 folds são usados para **treino**
   - 1 fold é usado para **teste**
3. O processo se repete 30 vezes, cada fold sendo usado uma vez como teste
4. As métricas finais são a **média** das 30 iterações

```python
kf = KFold(n_splits=30, shuffle=True, random_state=42)
```

#### Por Que K-Fold?

!!! success "Vantagens"
    - **Uso eficiente dos dados:** Todo o dataset é usado para treino e teste
    - **Estimativa robusta:** 30 iterações reduzem a variância da avaliação
    - **Evita viés:** Não depende de uma única divisão train/test
    - **Ideal para datasets pequenos:** Aproveita ao máximo os 452 registros

!!! info "Alternativa: Holdout"
    O método holdout (divisão única 80/20) desperdiçaria dados e produziria estimativas menos confiáveis para um dataset deste tamanho.

## Modelos Comparados

### 1. Dummy Regressor (Baseline)

**Tipo:** Modelo de referência

**Descrição:** Não realiza aprendizado real. Prediz sempre a **média** do conjunto de treino.

**Objetivo:** Estabelecer um baseline mínimo. Qualquer modelo útil deve superar o Dummy.

```python
DummyRegressor(strategy='mean')
```

**Quando usar:** Como referência para validar se modelos mais complexos agregam valor.

---

### 2. Linear Regression

**Tipo:** Modelo linear paramétrico

**Descrição:** Estabelece uma relação linear entre features e target, minimizando o erro quadrático médio.

**Equação:**
$$
\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n
$$

**Vantagens:**
- Simples e interpretável
- Treinamento rápido
- Bom quando há relação linear

**Desvantagens:**
- Assume linearidade
- Sensível a outliers
- Não captura interações complexas

```python
LinearRegression()
```

---

### 3. Decision Tree Regressor

**Tipo:** Modelo baseado em árvore

**Descrição:** Constrói uma estrutura hierárquica de decisões, dividindo o espaço de features em regiões homogêneas.

**Como funciona:**
1. Escolhe a feature e o ponto de corte que melhor separam os dados
2. Divide recursivamente até um critério de parada
3. Cada folha contém a predição (média dos exemplos naquela região)

**Vantagens:**
- Captura relações não lineares
- Captura interações entre features automaticamente
- Interpretável (pode-se visualizar a árvore)

**Desvantagens:**
- Propenso a overfitting
- Instável (pequenas mudanças nos dados alteram a árvore)

```python
DecisionTreeRegressor(random_state=42)
```

---

### 4. K-Nearest Neighbors (KNN)

**Tipo:** Modelo baseado em instâncias

**Descrição:** Para uma nova observação, encontra os K exemplos mais próximos no treino e prediz a média dos seus valores.

**Como funciona:**
1. Calcula a distância (geralmente euclidiana) entre a nova entrada e todos os pontos de treino
2. Seleciona os K vizinhos mais próximos
3. Prediz a média dos valores desses vizinhos

**Vantagens:**
- Não paramétrico (sem suposições sobre a forma dos dados)
- Simples e intuitivo
- Eficaz para padrões locais

**Desvantagens:**
- Computacionalmente custoso na predição
- Sensível à escala das features (requer normalização)
- Performance degrada em altas dimensões

```python
KNeighborsRegressor()
```

---

### 5. Support Vector Regressor (SVR)

**Tipo:** Modelo baseado em margens

**Descrição:** Encontra uma função que aproxima os dados dentro de uma margem de tolerância (ε), minimizando erro e complexidade.

**Como funciona:**
1. Define uma margem de tolerância ao redor da função de predição
2. Ignora erros menores que ε (support vectors ficam na margem)
3. Penaliza erros maiores que ε
4. Pode usar kernels para capturar não-linearidades

**Vantagens:**
- Robusto a outliers
- Eficaz em altas dimensões
- Captura padrões complexos com kernels (RBF)

**Desvantagens:**
- Treinamento pode ser lento
- Escolha do kernel e hiperparâmetros é crítica
- Menos interpretável

```python
SVR()
```

---

### 6. Random Forest

**Tipo:** Ensemble de árvores (Bagging)

**Descrição:** Cria múltiplas árvores de decisão independentes e combina suas predições através da média.

**Como funciona:**
1. Para cada árvore:
   - Seleciona uma amostra aleatória dos dados (bootstrap)
   - Em cada divisão, considera apenas um subconjunto aleatório de features
2. Treina todas as árvores independentemente
3. Predição final = média das predições de todas as árvores

**Vantagens:**
- Reduz overfitting (comparado a uma única árvore)
- Robusto a outliers e ruído
- Captura interações complexas
- Menos sensível a hiperparâmetros

**Desvantagens:**
- Menos interpretável que uma única árvore
- Pode ser computacionalmente custoso
- Memória necessária para armazenar múltiplas árvores

```python
RandomForestRegressor(random_state=42)
```

---

### 7. Gradient Boosting

**Tipo:** Ensemble de árvores (Boosting)

**Descrição:** Constrói árvores sequencialmente, onde cada nova árvore corrige os erros das anteriores.

**Como funciona:**
1. Começa com uma predição simples (média)
2. Para cada iteração:
   - Calcula os resíduos (erros) da predição atual
   - Treina uma nova árvore para predizer esses resíduos
   - Adiciona a nova árvore ao modelo com um peso (learning rate)
3. Predição final = soma ponderada de todas as árvores

**Vantagens:**
- Geralmente atinge os melhores resultados
- Flexível (pode otimizar diferentes funções de perda)
- Captura padrões muito complexos

**Desvantagens:**
- Mais propenso a overfitting (requer tuning cuidadoso)
- Treinamento sequencial (mais lento)
- Menos interpretável

```python
GradientBoostingRegressor(random_state=42)
```

---

## Métricas de Avaliação

### R² (Coeficiente de Determinação)

**Fórmula:**
$$
R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}
$$

**Interpretação:**
- Varia de -∞ a 1
- R² = 1: Predições perfeitas
- R² = 0: Modelo equivalente à média (baseline)
- R² < 0: Modelo pior que predizer sempre a média

**Por quê usar:** Mede quanto da variância do target é explicada pelo modelo. Intuitivo e amplamente usado.

### MAE (Mean Absolute Error)

**Fórmula:**
$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|
$$

**Interpretação:**
- Erro médio absoluto em unidades do target
- MAE = 0: Predições perfeitas
- Quanto menor, melhor

**Por quê usar:** Fácil de interpretar (erro médio na mesma escala do target). Menos sensível a outliers que o MSE.

### MSE (Mean Squared Error)

**Fórmula:**
$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

**Interpretação:**
- Erro quadrático médio
- Penaliza mais erros grandes (devido ao quadrado)
- MSE = 0: Predições perfeitas

**Por quê usar:** Penaliza mais erros maiores, útil quando grandes desvios são inaceitáveis.

## Implementação da Validação

```python
# Definir métricas
scoring_metrics = {
    'r2': 'r2',
    'mae': 'neg_mean_absolute_error',
    'mse': 'neg_mean_squared_error'
}

# Para cada modelo
for name, model in models.items():
    # Criar pipeline completo
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])
    
    # Validação cruzada
    scores = cross_validate(
        pipeline, X, y, 
        cv=kf, 
        scoring=scoring_metrics
    )
    
    # Armazenar resultados
    all_results[name] = scores
```

**Importante:** O scikit-learn retorna MAE e MSE como valores **negativos** (para maximização). Por isso invertemos o sinal ao reportar os resultados.

## Otimização de Hiperparâmetros

Para o melhor modelo identificado (exceto Dummy e Linear Regression), aplicamos **GridSearchCV** para otimizar hiperparâmetros.

### Grids de Busca

#### Decision Tree
```python
{
    'model__max_depth': [10, 20, None],
    'model__min_samples_leaf': [1, 2, 4],
    'model__max_features': ['sqrt', 'log2', None]
}
```

#### KNN
```python
{
    'model__n_neighbors': [3, 5, 7, 9],
    'model__weights': ['uniform', 'distance'],
    'model__p': [1, 2]  # Manhattan vs Euclidean
}
```

#### SVR
```python
{
    'model__C': [0.1, 1, 10],
    'model__kernel': ['linear', 'rbf'],
    'model__epsilon': [0.01, 0.1]
}
```

#### Random Forest
```python
{
    'model__n_estimators': [100, 200],
    'model__max_depth': [10, 20, None],
    'model__min_samples_leaf': [1, 2]
}
```

#### Gradient Boosting
```python
{
    'model__n_estimators': [100, 200],
    'model__learning_rate': [0.01, 0.1],
    'model__max_depth': [3, 5]
}
```

### Execução do GridSearchCV

```python
grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=grid_to_use,
    cv=10,  # 10 folds (mais rápido que 30)
    scoring='r2',
    n_jobs=-1,  # Usa todos os processadores
    verbose=1
)

grid_search.fit(X, y)

print(f"Melhor R²: {grid_search.best_score_:.4f}")
print(f"Melhores parâmetros: {grid_search.best_params_}")
```

## Análise de Estabilidade

Além das médias, analisamos a **distribuição** dos scores através de boxplots das 30 iterações.

**O que buscamos:**
- **Mediana alta:** Performance central boa
- **IQR pequeno:** Modelo estável (pouca variação entre folds)
- **Poucos outliers:** Comportamento consistente

**Modelos instáveis** (grande variância) podem ter boa média mas serem imprevisíveis em produção.

## Próximos Passos

Com os modelos treinados e validados, analisamos:

- [Resultados](results.md) - Performance comparativa e conclusões finais
