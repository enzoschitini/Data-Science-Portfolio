# **Predição de Aprovação de Cartão de Crédito: Desvendando os Fatores Críticos**
Enzo Schitini - 06 Agoso 2024

## **Manual de Análise - Credit Card Approval Prediction**

O objetivo deste manual é capacitar você a explorar, limpar e analisar dados armazenados em um DataFrame. Vamos abordar desde as etapas iniciais de carregamento e visualização dos dados até técnicas avançadas de análise e interpretação dos resultados.

### **Descrição do Projeto:**

O projeto "Previsão de Aprovação de Cartão de Crédito" busca desenvolver um modelo preditivo para otimizar o processo de concessão de crédito, minimizando os riscos financeiros associados à inadimplência. Em um cenário econômico onde o crédito desempenha um papel crucial, as instituições financeiras enfrentam o desafio constante de avaliar com precisão a capacidade de um cliente de honrar suas obrigações de crédito.

### **Contexto e Problema**

Com o aumento do uso de cartões de crédito, é essencial que as instituições financeiras possam tomar decisões informadas sobre a concessão de crédito. Uma decisão inadequada pode resultar em perdas financeiras significativas, seja pela concessão de crédito a clientes com alta probabilidade de inadimplência, ou pela rejeição de clientes com bom potencial de crédito. A utilização de técnicas de machine learning pode transformar a forma como essas decisões são feitas, tornando o processo mais eficiente e preciso.

### **Objetivo**

O objetivo deste projeto é construir um modelo de machine learning que seja capaz de prever se um cliente será aprovado ou rejeitado para um cartão de crédito com base em seu perfil financeiro e pessoal. Para isso, trabalhamos com um conjunto de dados históricos que inclui informações sobre o comportamento de crédito dos clientes, suas características demográficas e dados financeiros. O modelo desenvolvido visa não apenas prever a aprovação ou rejeição, mas também identificar quais características são mais influentes na decisão de crédito.

### **Metodologia**

1. **Coleta e Preparação dos Dados:** Inicialmente, foram coletados dados históricos de clientes, incluindo variáveis como idade, renda, histórico de crédito, entre outros. Os dados foram pré-processados para lidar com valores ausentes, dados inconsistentes e normalização.
2. **Análise Exploratória dos Dados:** Realizamos uma análise exploratória para entender as distribuições dos dados, identificar padrões e relações entre as variáveis. Esta etapa é crucial para ajustar o modelo e selecionar as características mais relevantes.
3. **Modelagem e Avaliação:** Utilizamos diversos algoritmos de machine learning, incluindo regressão logística, árvores de decisão e redes neurais, para treinar o modelo. O desempenho do modelo foi avaliado com base em métricas como acurácia, precisão, recall e AUC-ROC. Ajustes foram feitos para otimizar a performance e reduzir o risco de overfitting.
4. **Implementação e Validação:** Após a seleção do modelo final, realizamos a validação cruzada para garantir a robustez e a generalização dos resultados. O modelo foi então aplicado a um conjunto de dados de teste para avaliar seu desempenho em condições reais.

### **Resultados**

O modelo desenvolvido demonstrou uma capacidade significativa de prever com precisão a aprovação ou rejeição de solicitações de crédito. As análises mostraram quais fatores tiveram maior impacto nas decisões de crédito e forneceram insights valiosos para aprimorar o processo de avaliação.

### **Conclusão**

Este projeto não apenas contribui para uma tomada de decisão mais informada e eficiente na concessão de crédito, mas também oferece uma base sólida para futuras pesquisas e melhorias. A aplicação de técnicas avançadas de machine learning permite às instituições financeiras reduzir o risco e otimizar a alocação de recursos de crédito.

### **Próximos Passos**

Para aprimorar ainda mais o modelo, futuras etapas podem incluir a integração de dados adicionais, o uso de técnicas mais avançadas de machine learning e a aplicação do modelo em um ambiente real para avaliar seu desempenho e impacto no processo de concessão de crédito.

---

## Analisando o Perfil Financeiro e Pessoal para Decisões de Crédito Mais Precisas

### **Descrição Detalhada:**

Este projeto ambiciona construir um modelo de machine learning que preveja a aprovação ou rejeição de um cliente para um cartão de crédito, com base em informações detalhadas sobre seu perfil financeiro e pessoal. Utilizando um conjunto de dados históricos, a análise exploratória fornecerá insights valiosos sobre o comportamento de crédito dos clientes, suas características demográficas e dados financeiros. O objetivo final é desenvolver um modelo preditivo robusto, capaz não apenas de classificar os clientes como aprovados ou rejeitados, mas também de identificar as características mais influentes na tomada de decisão de crédito.

A análise exploratória profunda irá desvendar as nuances presentes no conjunto de dados, revelando padrões e tendências ocultas. Através de técnicas estatísticas e de visualização de dados, a análise irá investigar a relação entre variáveis como: 

- **Perfil Financeiro:** Renda, histórico de crédito, dívidas, patrimônio e gastos. Características
- **Demográficas:** Gênero, idade, estado civil, nível de escolaridade e tipo de trabalho.
- **Comportamento Financeiro:** Histórico de pagamentos, uso de crédito, movimentações bancárias.

Com base nas descobertas da análise exploratória, o projeto utilizará algoritmos de machine learning para construir um modelo preditivo de alta performance. O modelo será treinado com os dados históricos e avaliado em sua capacidade de prever a aprovação ou rejeição de novos clientes, com base em suas características individuais. 

A fase de avaliação do modelo será crucial para garantir a sua precisão e confiabilidade. Métodos como a validação cruzada e a análise de performance serão utilizados para determinar a eficácia do modelo em diferentes cenários e datasets. 

O modelo preditivo, além de auxiliar na tomada de decisão de crédito, fornecerá insights valiosos para a estratégia de negócio. A identificação das características mais influentes na aprovação ou rejeição permitirá a otimização dos processos de análise de crédito, a personalização de ofertas e o desenvolvimento de campanhas de marketing mais eficazes.

### **Importância do Projeto:**

A concessão de crédito é um processo complexo que exige análises detalhadas para minimizar o risco de inadimplência. Modelos de machine learning para predição de aprovação de cartão de crédito oferecem diversas vantagens, como: 

- **Tomada de Decisão Automatizada e Eficiente:** A análise de crédito manual é um processo demorado e sujeito a erros humanos. Modelos de machine learning podem automatizar essa tarefa, tornando a análise mais rápida e precisa.
- **Redução do Risco de Inadimplência:** Modelos preditivos podem identificar clientes com maior probabilidade de inadimplência, permitindo que as instituições financeiras tomem medidas preventivas.
- **Aprimoramento da Experiência do Cliente:** A aprovação de crédito mais rápida e eficiente proporciona uma experiência mais satisfatória para os clientes.
- **Identificação de Oportunidades de Negócio:** A análise dos dados de crédito permite identificar potenciais clientes e oportunidades de expansão do negócio.

## **Pilares da Análise:**

### **1. Demografia e Características Socioeconômicas:**

- **CODE_GENDER:** A análise da relação entre gênero e aprovação de crédito pode revelar possíveis vieses e desigualdades, além de fornecer insights sobre o perfil de clientes que mais solicitam crédito.
- **FLAG*OWN*CAR:** A posse de carro pode ser um indicador de renda e capacidade de pagamento. Analisar a relação com a aprovação de crédito pode revelar se essa variável influencia a decisão do banco.
- **FLAG*OWN*REALTY:**  A posse de imóveis, assim como a posse de carro, pode ser um indicador de capacidade de pagamento. A relação entre a posse de imóveis e a aprovação de crédito deve ser investigada para verificar se essa variável é relevante.
- **CNT_CHILDREN:** O número de dependentes pode influenciar o orçamento familiar e a capacidade de pagamento. A relação entre o número de filhos e a aprovação de crédito deve ser analisada para identificar se essa variável é um fator determinante.
- **AMT*INCOME*TOTAL:** A renda total do cliente é um indicador crucial da capacidade de pagamento. Analisar a relação entre renda e aprovação de crédito é fundamental para entender quais faixas de renda têm maior probabilidade de aprovação.
- **NAME*INCOME*TYPE:**  A fonte de renda pode influenciar a estabilidade financeira do cliente. A análise da relação entre o tipo de renda e a aprovação de crédito pode revelar quais tipos de renda são mais propensos a aprovação.
- **NAME*EDUCATION*TYPE:** O nível de educação pode estar relacionado ao poder aquisitivo e ao perfil de risco do cliente. Analisar a relação entre o nível de educação e a aprovação de crédito pode revelar se essa variável é um fator relevante na decisão do banco.

---

### **2. Situação Familiar e Habitacional:**

- **NAME*FAMILY*STATUS:**  A situação familiar pode influenciar o orçamento e as responsabilidades financeiras do cliente. Analisar a relação entre o estado civil e a aprovação de crédito pode fornecer insights sobre como o banco avalia esse fator.
- **NAME*HOUSING*TYPE:** O tipo de moradia pode ser um indicador do padrão de vida e da situação financeira do cliente. Analisar a relação entre o tipo de moradia e a aprovação de crédito pode revelar se essa variável é um fator relevante para o banco.
- **CNT*FAM*MEMBERS:** O número de membros da família pode influenciar o orçamento familiar. Analisar a relação entre o número de membros da família e a aprovação de crédito pode revelar como o banco leva em consideração esse fator.

---

### **3. Histórico de Emprego e Comunicação:**

- **DAYS_BIRTH:** A idade do cliente pode ser um indicador de experiência profissional e estabilidade financeira. Analisar a relação entre a idade e a aprovação de crédito pode revelar se essa variável é um fator relevante para o banco.
- **DAYS_EMPLOYED:** A duração do tempo de trabalho pode ser um indicador de experiência profissional e estabilidade financeira. Analisar a relação entre o tempo de emprego e a aprovação de crédito pode revelar se essa variável é um fator determinante.
- **FLAG_MOBIL:** A posse de telefone celular é um indicador de acessibilidade e comunicação. Analisar a relação entre a posse de celular e a aprovação de crédito pode revelar se essa variável é um fator relevante para o banco.
- **FLAG*WORK*PHONE:**  A posse de telefone comercial pode ser um indicador de profissionalismo e acessibilidade. Analisar a relação entre a posse de telefone comercial e a aprovação de crédito pode revelar se essa variável é um fator relevante para o banco.
- **FLAG_PHONE:**  A posse de telefone fixo pode ser um indicador de estabilidade residencial e comunicação. Analisar a relação entre a posse de telefone fixo e a aprovação de crédito pode revelar se essa variável é um fator relevante para o banco.
- **FLAG_EMAIL:**  A posse de email pode ser um indicador de acesso à informação e comunicação digital. Analisar a relação entre a posse de email e a aprovação de crédito pode revelar se essa variável é um fator relevante para o banco.

---

### **4.  Profissão e Informações Adicionais:**

- **OCCUPATION_TYPE:** A profissão do cliente pode ser um indicador de renda e estabilidade financeira. Analisar a relação entre a profissão e a aprovação de crédito pode revelar se essa variável é um fator relevante para o banco.
- **Default:** A variável 'Default' indica se o cliente já teve problemas de crédito no passado. Analisar a relação entre essa variável e a aprovação de crédito é fundamental para entender o histórico de crédito dos clientes e prever a probabilidade de inadimplência.

---

Esses pilares, combinados com a análise de outras variáveis, permitirão gerar insights profundos sobre os fatores que influenciam a aprovação de crédito e construir um modelo preditivo mais preciso e eficaz.

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

## **Análise Descritiva**

**Hipóteses:**

1. Clientes com maior renda tendem a ter menos filhos.

2. Clientes com maior tempo de trabalho tendem a ter maior renda.

3. Clientes com nível de escolaridade mais alto tendem a ter maior renda.

4. Clientes com imóvel próprio são menos propensos a entrar em "Default".

5. Clientes com mais dependentes tendem a ter menor renda.

6. Clientes com profissões mais qualificadas tendem a ter maior renda.

7. A idade do cliente é um fator relevante na previsão de "Default".

8. Clientes com acesso a mais meios de comunicação são menos propensos a entrar em "Default".

9. O tipo de família e moradia influenciam o risco de "Default".

10. Existe uma correlação negativa entre o tempo de trabalho e o risco de "Default".