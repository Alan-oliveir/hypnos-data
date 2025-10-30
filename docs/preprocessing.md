# Pré-processamento e Engenharia de Features

## Objetivos

O pré-processamento tem como objetivos:

1. Tratar valores faltantes
2. Transformar variáveis temporais em features numéricas
3. Normalizar variáveis numéricas
4. Codificar variáveis categóricas
5. Criar um pipeline reproduzível

## Limpeza de Dados

### Remoção de Colunas

A coluna **ID** foi removida, pois é apenas um identificador e não contém informação preditiva.

```python
df_processed = df_processed.drop(columns=['ID'])
```

### Tratamento de Valores Faltantes

Foram identificados valores faltantes nas seguintes variáveis:

- Awakenings
- Caffeine consumption
- Alcohol consumption
- Exercise frequency

**Estratégia Adotada:** Imputação pela **mediana**

**Justificativa:** A mediana é mais robusta a outliers do que a média, sendo adequada para variáveis que podem ter valores extremos.

```python
median_cols = ['Awakenings', 'Caffeine consumption', 
               'Alcohol consumption', 'Exercise frequency']

for col in median_cols:
    median_val = df_tratado[col].median()
    df_tratado[col] = df_tratado[col].fillna(median_val)
```

## Engenharia de Features

### Transformação de Variáveis Temporais

Os horários de dormir e acordar foram convertidos para features cíclicas usando funções seno e cosseno.

**Por quê?** Horários são cíclicos (23h está próximo de 0h), e a representação tradicional não captura essa ciclicidade. As funções trigonométricas resolvem esse problema.

#### Bedtime (Hora de Dormir)

```python
df_processed['bedtime_hour_sin'] = np.sin(
    df_processed['Bedtime'].dt.hour * (2. * np.pi / 24)
)
df_processed['bedtime_hour_cos'] = np.cos(
    df_processed['Bedtime'].dt.hour * (2. * np.pi / 24)
)
```

#### Wakeup Time (Hora de Acordar)

```python
df_processed['wakeup_hour_sin'] = np.sin(
    df_processed['Wakeup time'].dt.hour * (2. * np.pi / 24)
)
df_processed['wakeup_hour_cos'] = np.cos(
    df_processed['Wakeup time'].dt.hour * (2. * np.pi / 24)
)
```

**Resultado:** 4 novas features cíclicas que capturam melhor a natureza temporal dos horários.

### Padronização de Nomes

Colunas foram renomeadas para o padrão **snake_case** para facilitar o uso no código:

```python
df_processed.columns = [col.replace(' ', '_').lower() 
                        for col in df_processed.columns]
```

Exemplos de transformação:
- `Sleep efficiency` → `sleep_efficiency`
- `Caffeine consumption` → `caffeine_consumption`

## Pipeline de Pré-processamento

### Separação de Features e Target

```python
TARGET = 'sleep_efficiency'
X = df_processed.drop(columns=[TARGET])
y = df_processed[TARGET]
```

### Identificação de Tipos de Variáveis

```python
numeric_features = X.select_dtypes(include=np.number).columns.tolist()
categorical_features = X.select_dtypes(exclude=np.number).columns.tolist()
```

**Variáveis Numéricas:** age, sleep_duration, awakenings, caffeine_consumption, alcohol_consumption, exercise_frequency, bedtime_hour_sin, bedtime_hour_cos, wakeup_hour_sin, wakeup_hour_cos, rem_sleep_percentage, deep_sleep_percentage, light_sleep_percentage

**Variáveis Categóricas:** gender, smoking_status

### Pipeline para Variáveis Numéricas

```python
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
```

**Etapas:**

1. **SimpleImputer:** Preenche valores faltantes com a mediana
2. **StandardScaler:** Normaliza as variáveis (média 0, desvio padrão 1)

**Por quê normalizar?** Algoritmos como SVM, KNN e Regressão Linear são sensíveis à escala das variáveis. A normalização garante que todas as features tenham o mesmo peso inicial.

### Pipeline para Variáveis Categóricas

```python
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
])
```

**Etapas:**

1. **SimpleImputer:** Preenche valores faltantes com a moda (valor mais frequente)
2. **OneHotEncoder:** Converte categorias em variáveis binárias (0 e 1)
   - `handle_unknown='ignore'`: Lida com categorias não vistas no treino
   - `drop='first'`: Remove uma categoria para evitar multicolinearidade

**Exemplo de Encoding:**

| Gender Original | gender_Male |
|----------------|-------------|
| Female         | 0           |
| Male           | 1           |

### ColumnTransformer

O `ColumnTransformer` aplica os pipelines apropriados para cada tipo de variável:

```python
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ],
    remainder='passthrough'
)
```

### Resultado do Pré-processamento

Após aplicar o pipeline:

```python
X_processed = preprocessor.fit_transform(X)
print(f"Dimensões: {X_processed.shape}")
# Output: Dimensões: (452, 15)
```

O dataset processado está pronto para ser usado nos modelos de Machine Learning.

## Vantagens do Pipeline

### Reprodutibilidade

O pipeline garante que o mesmo pré-processamento será aplicado de forma consistente:

- Nos dados de treino
- Nos dados de validação
- Nos dados de teste
- Em dados futuros (produção)

### Prevenção de Data Leakage

O pipeline garante que:

1. A imputação usa estatísticas calculadas **apenas no conjunto de treino**
2. A normalização usa média/desvio padrão **apenas do treino**
3. O OneHotEncoder conhece **apenas as categorias do treino**

Isso evita que informações do conjunto de teste "vazem" para o treino, o que causaria overfitting e superestimação da performance.

### Integração com Scikit-Learn

O pipeline se integra perfeitamente com:

- **Cross-validation:** `cross_validate(pipeline, X, y, cv=kfold)`
- **GridSearchCV:** Permite otimizar hiperparâmetros do pré-processamento e do modelo simultaneamente
- **Modelos finais:** O pipeline inteiro pode ser salvo e carregado

```python
# Exemplo de uso
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

## Resumo das Transformações

| Etapa | Entrada | Saída | Justificativa |
|-------|---------|-------|---------------|
| **Conversão temporal** | Bedtime, Wakeup time (datetime) | 4 features cíclicas (sin, cos) | Captura ciclicidade dos horários |
| **Imputação numérica** | Features com NaN | Features completas (mediana) | Mantém distribuição, robusta a outliers |
| **Normalização** | Features em escalas diferentes | Features normalizadas (μ=0, σ=1) | Equaliza importância inicial |
| **Imputação categórica** | Categorias com NaN | Categorias completas (moda) | Usa valor mais comum |
| **One-Hot Encoding** | gender, smoking_status | Variáveis binárias | Formato numérico para modelos |

## Próximos Passos

Com os dados pré-processados, avançamos para:

- [Modelagem](modeling.md) - Treinamento e comparação de modelos
- [Resultados](results.md) - Análise de performance e conclusões
