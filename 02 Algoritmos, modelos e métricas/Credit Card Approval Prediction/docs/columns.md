## **Análise das colunas do dataset:**

O dataset parece conter informações sobre clientes de um banco, com foco em dados demográficos, financeiros e de trabalho, além de uma coluna que indica se o cliente teve ou não um default (inadimplência) em seus pagamentos. Vamos analisar cada coluna:

---

**1. Variáveis Demográficas:**

- **CODE_GENDER:**  Gênero do cliente (M - Masculino, F - Feminino)
- **FLAG*OWN*CAR:** Indica se o cliente possui carro (Y - Sim, N - Não)
- **FLAG*OWN*REALTY:** Indica se o cliente possui imóvel próprio (Y - Sim, N - Não)
- **CNT_CHILDREN:** Número de filhos do cliente
- **DAYS_BIRTH:** Número de dias desde o nascimento do cliente. (Valores negativos indicam que o cliente nasceu antes da data de referência, provavelmente a data da coleta dos dados)
- **CNT*FAM*MEMBERS:** Número de membros da família do cliente

---

**2. Variáveis Financeiras:**

- **AMT*INCOME*TOTAL:** Renda total anual do cliente.

---

**3. Variáveis de Trabalho:**

- **NAME*INCOME*TYPE:** Tipo de renda do cliente (ex: Working, Commercial associate, Pensioner)
- **NAME*EDUCATION*TYPE:** Nível de escolaridade do cliente (ex: Higher education, Secondary / secondary special)
- **NAME*FAMILY*STATUS:** Estado civil do cliente (ex: Married, Single / not married, Civil marriage)
- **NAME*HOUSING*TYPE:** Tipo de moradia do cliente (ex: House / apartment, Rented apartment, With parents)
- **DAYS_EMPLOYED:** Número de dias desde o início do emprego atual do cliente. (Valores negativos indicam que o cliente está empregado antes da data de referência, provavelmente a data da coleta dos dados)

---

**4. Variáveis de Comunicação:**

- **FLAG_MOBIL:** Indica se o cliente possui telefone móvel (1 - Sim, 0 - Não)
- **FLAG*WORK*PHONE:** Indica se o cliente possui telefone comercial (1 - Sim, 0 - Não)
- **FLAG_PHONE:** Indica se o cliente possui telefone fixo (1 - Sim, 0 - Não)
- **FLAG_EMAIL:** Indica se o cliente possui email (1 - Sim, 0 - Não)

---

**5. Variável de Ocupação:**

- **OCCUPATION_TYPE:** Tipo de ocupação do cliente (ex: Security staff, Sales staff, etc.)

---

**6. Variável Alvo:**

- ***Default:**  Indica se o cliente teve* default* (inadimplência) em seus pagamentos (1 - Sim, 0 - Não)

---

# Tabela:
#### Esse datafame contém 18 colunas e 95027 linhas

| Nome                 | Tipo           | qnt_categorias | Dados nulos | Dados nulos % |
|----------------------|----------------|----------------|-------------|---------------|
| CODE_GENDER          | str            | 2              | 0           | 0.0           |
| FLAG_OWN_CAR         | str            | 2              | 0           | 0.0           |
| FLAG_OWN_REALTY      | str            | 2              | 0           | 0.0           |
| CNT_CHILDREN         | numpy.int64    | 12             | 0           | 0.0           |
| AMT_INCOME_TOTAL     | numpy.float64  | 866            | 0           | 0.0           |
| NAME_INCOME_TYPE     | str            | 5              | 0           | 0.0           |
| NAME_EDUCATION_TYPE  | str            | 5              | 0           | 0.0           |
| NAME_FAMILY_STATUS   | str            | 5              | 0           | 0.0           |
| NAME_HOUSING_TYPE    | str            | 6              | 0           | 0.0           |
| DAYS_BIRTH           | numpy.int64    | 16379          | 0           | 0.0           |
| DAYS_EMPLOYED        | numpy.int64    | 9406           | 0           | 0.0           |
| FLAG_MOBIL           | numpy.int64    | 1              | 0           | 0.0           |
| FLAG_WORK_PHONE      | numpy.int64    | 2              | 0           | 0.0           |
| FLAG_PHONE           | numpy.int64    | 2              | 0           | 0.0           |
| FLAG_EMAIL           | numpy.int64    | 2              | 0           | 0.0           |
| OCCUPATION_TYPE      | float          | 18             | 28967       | 30.0          |
| CNT_FAM_MEMBERS      | numpy.float64  | 13             | 0           | 0.0           |
| Default              | numpy.int64    | 2              | 0           | 0.0           |

---

## **Engenharia de Atributos:**

Com base nas colunas existentes, podemos criar novas colunas (atributos) para melhorar a qualidade dos dados e aprimorar o modelo de machine learning:

**1. Transformando Datas em Informações Úteis:**

- **AGE:** Criar uma coluna 'AGE' calculando a idade do cliente a partir de `DAYS_BIRTH` (dividindo por 365).
- **YEARS*EMPLOYED:** Criar uma coluna 'YEARS*EMPLOYED' calculando o tempo de emprego do cliente a partir de `DAYS_EMPLOYED` (dividindo por 365).
- **AGE*AT*EMPLOYMENT:** Criar uma coluna calculando a idade do cliente no momento em que ele começou a trabalhar (AGE - YEARS_EMPLOYED).

**2. Combinando Variáveis Categoricas:**

- **INCOME*TYPE*EDUCATION:** Criar uma coluna combinando `NAME[i]INCOME[/i]TYPE` e `NAME[i]EDUCATION[/i]TYPE`, para identificar grupos de clientes com características semelhantes.

**3. Criando Indicadores Financeiros:**

- **INCOME*PER*FAMILY*MEMBER:** Criar uma coluna calculando a renda per capita da família, dividindo* `AMT` INCOME[i]TOTAL *por* `CNT` FAM_MEMBERS
- **INCOME*RATIO*TO_CHILDREN:** Criar uma coluna calculando a razão entre a renda total e o número de filhos, para identificar o peso da renda familiar por filho.

**4. Criando Indicadores de Perfil:**

- **HAS*EMAIL*AND_PHONE:** Criar uma coluna que indique se o cliente possui email e telefone, para identificar clientes com maior conectividade.

**5. Criando Indicadores de Risco:**

- ***AGEATDEFAULT:** Criar uma coluna calculando a idade do cliente no momento do* default
- ***YEARSEMPLOYEDAT_DEFAULT:** Criar uma coluna calculando o tempo de emprego do cliente no momento do* default


## **Métricas Básicas e Gráficos para Análise Inicial:**

**Objetivo:** Entender a distribuição dos dados, identificar padrões e possíveis relações entre as variáveis para prever a variável "Default" (Inadimplência).

**Métricas Básicas:**

- Média, mediana, desvio padrão, mínimo, máximo, quartis para todas as variáveis numéricas.
- Frequências absolutas e relativas para variáveis categóricas.
- Correlação de Pearson (para variáveis numéricas) para identificar relações lineares.
- Coeficiente de Cramer (para variáveis categóricas) para identificar relações não lineares.

**Gráficos:**

- **Histograma:** para visualizar a distribuição de cada variável numérica**.**
- **Boxplot:** para visualizar a distribuição de cada variável numérica e identificar outliers.
- **Gráfico de Barras:** para visualizar a frequência de cada categoria em variáveis categóricas.
- **Gráfico de Dispersão:** para visualizar a relação entre duas variáveis numéricas.
- **Matriz de Correlação:** para visualizar a correlação entre todas as variáveis numéricas.
- **Gráfico de Proporção:** para visualizar a proporção de inadimplentes (variável "Default") para cada categoria de variáveis categóricas.