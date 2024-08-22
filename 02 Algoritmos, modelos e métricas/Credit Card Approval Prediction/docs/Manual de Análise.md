## **Modelo Preditivo para Aprovação de Cartões de Crédito: Otimizando a Tomada de Decisão com Análise de Dados de Clientes**

Manual de Análise - 22 Agosto 2024

**Explorando o Perfil Ideal para Aprovação de Crédito**

Este projeto tem como objetivo desenvolver um modelo de machine learning para prever a aprovação de crédito para novos clientes de um banco. A análise se baseará em dados demográficos, financeiros e comportamentais de clientes existentes, com o intuito de identificar padrões que possam otimizar o processo de concessão de crédito.

**Visão Geral do Projeto:**

A aprovação de crédito é um processo crítico para instituições financeiras, impactando diretamente a lucratividade e a gestão de riscos. Com o aumento do volume de solicitações, a eficiência na análise e classificação dos candidatos tornou-se essencial. Nesse contexto, a análise de dados e o machine learning emergem como ferramentas poderosas para automatizar e aprimorar a tomada de decisão.

Este estudo utilizará um conjunto de dados reais que inclui informações de clientes de um banco, como:

- **Dados demográficos:** idade, sexo, número de dependentes, escolaridade, estado civil.
- **Dados financeiros:** renda anual, tipo de cartão, limite de crédito.
- **Dados comportamentais:** tempo de relacionamento com o banco, quantidade de produtos contratados, histórico de transações.

O projeto aplicará técnicas de machine learning, como regressão logística ou árvores de decisão, para construir um modelo preditivo capaz de identificar clientes com maior probabilidade de cumprir suas obrigações financeiras.

**Importância do Projeto:**

A implementação de um modelo preditivo para aprovação de crédito oferece diversos benefícios ao banco, incluindo:

- **Redução de riscos:** Identificação de clientes de alto risco para evitar concessões de crédito que possam resultar em inadimplência.
- **Aumento da lucratividade:** Aprovação de clientes com alta probabilidade de pagamento, ampliando o volume de crédito concedido.
- **Melhoria da experiência do cliente:** Agilização do processo de aprovação e oferta de soluções personalizadas aos clientes.
- **Otimização de recursos:** Direcionamento estratégico dos esforços de marketing e vendas para clientes com maior chance de aprovação.

**Pilares da Análise:**

A análise se concentrará em três pilares principais para extrair insights relevantes e construir um modelo preditivo eficaz:

1. **Análise Demográfica:**
2. **Análise Financeira:**
3. **Análise de Relacionamento:**

## **Engenharia de atributos**


**Descrição das Colunas do Dataset:**

1. **id**: Identificação única para cada cliente.
2. **default**: Indicador binário que mostra se o cliente está inadimplente (1) ou não (0).
3. **idade**: Idade do cliente em anos.
4. **sexo**: Gênero do cliente, onde 'M' representa Masculino e 'F' Feminino.
5. **dependentes**: Número de dependentes do cliente.
6. **escolaridade**: Nível de escolaridade do cliente.
7. **estado_civil**: Estado civil do cliente.
8. **salario_anual**: Faixa de renda anual do cliente.
9. **tipo_cartao**: Tipo de cartão de crédito que o cliente possui.
10. **mesesderelacionamento**: Duração do relacionamento do cliente com o banco em meses.
11. **qtd_produtos**: Quantidade de produtos financeiros que o cliente possui no banco.
12. **iteracoes_12m**: Número de interações do cliente com o banco nos últimos 12 meses.
13. **mesesinativo12m**: Número de meses que o cliente ficou inativo nos últimos 12 meses.
14. **limite_credito**: Limite de crédito disponível para o cliente.
15. **valortransacoes12m**: Valor total das transações realizadas pelo cliente nos últimos 12 meses.
16. **qtdtransacoes12m**: Número total de transações realizadas pelo cliente nos últimos 12 meses.

### **Esse datafame contém 16 colunas e 10127 linhas**

| Nome | Tipo | qnt_categorias | Dados nulos | Dados nulos % |
| --- | --- | --- | --- | --- |
| id | numpy.int64 | 10127 | 0 | 0.0% |
| default | numpy.int64 | 2 | 0 | 0.0% |
| idade | numpy.int64 | 45 | 0 | 0.0% |
| sexo | str | 2 | 0 | 0.0% |
| dependentes | numpy.int64 | 6 | 0 | 0.0% |
| escolaridade | str | 6 | 1519 | 15.0% |
| estado_civil | str | 4 | 749 | 7.0% |
| salario_anual | str | 6 | 1112 | 11.0% |
| tipo_cartao | str | 4 | 0 | 0.0% |
| meses_de_relacionamento | numpy.int64 | 44 | 0 | 0.0% |
| qtd_produtos | numpy.int64 | 6 | 0 | 0.0% |
| iteracoes_12m | numpy.int64 | 7 | 0 | 0.0% |
| meses_inativo_12m | numpy.int64 | 7 | 0 | 0.0% |
| limite_credito | str | 9272 | 0 | 0.0% |
| valor_transacoes_12m | str | 10035 | 0 | 0.0% |
| qtd_transacoes_12m | numpy.int64 | 126 | 0 | 0.0% |

#### **Grupos de colunas**

| Cliente | Tempo | Produto | Cartão | Financeiro |
| --- | --- | --- | --- | --- |
| id | meses_de_relacionamento | qtd_produtos | tipo_cartao | salario_anual |
| idade | iteracoes_12m |  |  | limite_credito |
| sexo | meses_inativo_12m |  |  |  |
| dependentes |  |  |  |  |
| escolaridade |  |  |  |  |
| estado_civil |  |  |  |  |


### **Criando novos Atributos:**

Com base nas colunas existentes, novas variáveis podem ser criadas para aprimorar a análise e o desempenho dos modelos preditivos:

1. **Informações Demográficas:**
    - **idade_faixa**: Categoriza a idade em faixas (ex: 18-25, 26-35, 36-45, etc.).
    - **relacao_dependentes**: Relação entre número de dependentes e idade (dependentes/idade).
    - **rendapercapita**: Renda per capita do cliente (salario_anual / (dependentes + 1)).
2. **Métricas Financeiras:**
    - **taxautilizacaocredito**: Taxa de utilização do limite de crédito (valortransacoes12m / limite_credito).
    - **valormediotransacao**: Valor médio de cada transação (valortransacoes12m / qtdtransacoes12m).
    - **transacoespormes**: Média de transações por mês (qtdtransacoes12m / 12).
3. **Informações de Comportamento:**
    - **mesesativos12m**: Número de meses ativos nos últimos 12 meses (12 - mesesinativo12m).
    - **frequenciainteracao**: Frequência de interação do cliente com o banco (iteracoes_12m / mesesativos12m).
    - **relacaoprodutosidade**: Relação entre quantidade de produtos e idade do cliente (qtd_produtos / idade).
4. **Combinação de Atributos:**
    - **idadeestadocivil**: Combinação da idade com o estado civil (ex: 30-40 Anos Casado, 40-50 Anos Solteiro, etc.).
    - **escolaridade_renda**: Combinação do nível de escolaridade com a faixa salarial (ex: Ensino Médio $40K - $60K, Mestrado $80K - $120K, etc.).
5. **Atributos Categóricos:**
    - **faixa_idade**: Atributo categórico que classifica a idade em grupos (ex: Jovem, Adulto, Idoso).
    - **renda_alta**: Atributo binário (0 ou 1) que indica se a renda do cliente é alta (acima de $80K).
    - **produto_alto**: Atributo binário (0 ou 1) que indica se o cliente possui mais de 3 produtos.

---

## **Análises Exploratória (EDA)**

Para uma visão inicial do arquivo CSV, é possível analisar as seguintes métricas e realizar algumas análises:

**Plano da EDA:**

1. **Estatísticas Descritivas**: Cálculo de média, mediana, desvio padrão, mínimo e máximo para as colunas numéricas (idade, dependentes, qtdprodutos, iteracoes12m, mesesinativo12m, limitecredito, valortransacoes12m, qtdtransacoes_12m).
2. **Contagem de Valores Únicos**: Contagem dos valores únicos para as colunas categóricas (sexo, escolaridade, estadocivil, tipocartao).
3. **Distribuição de Frequência**: Análise da distribuição de frequência para colunas categóricas e numéricas, visualizando a frequência de cada valor.
4. **Análise Univariada**
5. **Análise de Outliers**: Identificação de valores discrepantes nas variáveis numéricas, que podem indicar erros nos dados ou casos especiais.
6. **Correlação entre Variáveis**: Análise da correlação entre as variáveis numéricas, utilizando gráficos de dispersão ou o cálculo do coeficiente de correlação.

## **Análises Descritiva**

**Plano da EDA:**

1. **Setup de Análise**

2. **Análise Bivariada**

3. **Análise de Grupos**: Identificação de padrões e agrupamentos de clientes com base em suas características, aplicando técnicas de clusterização.

4. **Análise dos Fatores:**
    - **Idade**: Avaliar a distribuição etária dos clientes, identificando faixas etárias com maior concentração, comportamento de compra e diferenças no uso de produtos e serviços.
    - **Sexo**: Comparar o comportamento de compra entre homens e mulheres, observando diferenças em preferências, gastos e uso de produtos.
    - **Dependentes**: Analisar como o número de dependentes influencia o comportamento de compra, consumo e uso de produtos e serviços.
    - **Escolaridade**: Explorar a relação entre o nível de escolaridade e o comportamento de compra, incluindo tipos de produtos adquiridos, valor médio das transações e frequência de compras.
    - **Estado Civil**: Comparar o comportamento de compra entre diferentes estados civis, observando variações nas preferências, gastos e uso de produtos.
    - **Salário Anual**: Analisar a relação entre a faixa salarial e o comportamento de compra, considerando o tipo de produtos adquiridos, valor médio das transações e frequência de compras.
    - **Tipo de Cartão**: Investigar as diferenças no comportamento de compra entre tipos de cartão, analisando valor médio das transações, frequência de compras e uso de serviços adicionais.
    - **Meses de Relacionamento**: Analisar a evolução do comportamento de compra ao longo do tempo, considerando a fidelidade dos clientes e o impacto da duração do relacionamento no valor e frequência das transações.
    - **Meses Inativo em 12m**: Estudar os clientes inativos nos últimos 12 meses, identificando motivos para a inatividade e características que os diferenciam dos ativos.
    - **Interações em 12m**: Analisar a frequência de interação dos clientes com a empresa nos últimos 12 meses, e sua relação com comportamento de compra e fidelidade.
    - **Quantidade de Produtos**: Analisar a quantidade de produtos que os clientes possuem, identificando sinergias entre produtos e impacto no valor e frequência das transações.
    - **Limite de Crédito**: Investigar a relação entre o limite de crédito e o comportamento de compra, incluindo valor médio das transações, frequência de compras e uso do limite disponível.
    - **Valor das Transações em 12m**: Analisar o valor total das transações nos últimos 12 meses, identificando padrões de gastos e principais categorias de produtos e serviços adquiridos.
    - **Quantidade de Transações em 12m**: Estudar a frequência das transações nos últimos 12 meses, identificando padrões de comportamento e o impacto da frequência de compras no valor total das transações.

## **Análises do Default**

**Planejamento da Análise:**

**Objetivo:** Identificar as variáveis que influenciam o risco de default e compreender o impacto de cada uma no comportamento dos clientes.

**Variáveis de Interesse:**

- **Demográficas:** idade, renda, estado civil, número de dependentes, escolaridade, profissão.
- **Financeiras:** histórico de crédito, score de crédito, dívida total, renda disponível, patrimônio líquido, valor do empréstimo, taxa de juros, prazo do empréstimo.
- **Comportamentais:** histórico de pagamentos, número de atrasos, valor de parcelas atrasadas, utilização do limite de crédito, histórico de solicitações de crédito.
- **De Mercado:** taxa de juros do mercado, índice de inflação, taxa de desemprego, condições econômicas gerais.

**Perguntas de Pesquisa:**

- Quais variáveis são mais significativas para prever o risco de default?
- Qual é a relação entre as variáveis e a probabilidade de default?
- Como a combinação de diferentes variáveis impacta o risco de default?
- Existem grupos distintos de clientes com perfis de risco diferentes?
- Como os resultados da análise podem ser usados para melhorar as decisões de crédito e reduzir as perdas por default?

**2. Criação do Cubo de Dados**

**Dimensões:**

- **Cliente:** ID, dados demográficos, histórico de crédito, comportamento de pagamento, etc.
- **Empréstimo:** Valor, taxa de juros, prazo, data de concessão, etc.
- **Tempo:** Data de pagamento, vencimento, solicitação, etc.
- **Mercado:** Taxa de juros do mercado, inflação, desemprego, etc.

**Fatores:**

- **Demográficos:** idade, renda, estado civil, número de dependentes, etc.
- **Financeiros:** histórico de crédito, score de crédito, dívida total, etc.
- **Comportamentais:** histórico de pagamentos, número de atrasos, etc.
- **De Mercado:** taxa de juros do mercado, índice de inflação, etc.

**Medidas:**

- **Contagem:** Número de clientes, empréstimos, defaults.
- **Taxas:** Default, inadimplência, utilização do crédito.
- **Média:** Idade média, renda média, valor médio do empréstimo.
- **Proporção:** Clientes com histórico de crédito positivo, clientes com renda acima da média.
- **Distribuição:** Idade dos clientes, renda, valor do empréstimo.

**3. Geração de Hipóteses**

- **Hipótese 1:** Clientes com histórico de crédito negativo e score baixo têm maior probabilidade de default.
- **Hipótese 2:** Clientes com alta dívida total e baixa renda disponível apresentam maior risco de default.
- **Hipótese 3:** A taxa de juros do mercado influencia a taxa de default, com taxas mais altas associadas a maior probabilidade de default.
- **Hipótese 4:** Clientes com maior número de atrasos em pagamentos anteriores têm maior probabilidade de default.
- **Hipótese 5:** Clientes mais jovens e com menor renda tendem a ter maior risco de default.

**4. Análises Adicionais**

- **Clusterização:** Para identificar grupos distintos de clientes com perfis de risco diferentes.
- **ANOVA:** Para comparar as médias de risco de default entre diferentes grupos de clientes.
- **ANCOVA:** Para avaliar o impacto das variáveis independentes e covariáveis no risco de default.

**5. Insights e Impacto da Análise**

A análise do impacto das variáveis no default pode gerar insights valiosos para decisões de crédito:

- **Identificação de fatores de risco:** Identificar as variáveis que influenciam o risco de default permite construir modelos de scoring de crédito mais precisos.
- **Gestão de risco:** Entender o impacto de cada variável no risco de default possibilita a implementação de estratégias de gestão de risco mais eficazes.
- **Segmentação de clientes:** Segmentar clientes em grupos de risco diferentes permite oferecer produtos personalizados e ajustar políticas de crédito conforme o perfil de risco.
- **Otimização de decisões de crédito:** Os resultados da análise podem melhorar a tomada de decisões de crédito, reduzindo as taxas de default e aumentando a lucratividade.
- **Melhoria da estratégia de marketing:** Compreender o perfil dos clientes com maior risco de default possibilita campanhas de marketing mais direcionadas e eficazes.

## **Hipóteses:**

1. Clientes com maior renda tendem a possuir um limite de crédito mais elevado.
2. Clientes com mais dependentes têm, em média, um limite de crédito mais alto.
3. Clientes com maior nível de escolaridade tendem a ter limites de crédito superiores.
4. Clientes mais velhos geralmente têm limites de crédito mais altos.
5. Clientes com maior tempo de relacionamento com o banco tendem a possuir limites de crédito mais elevados.
6. Clientes que utilizam mais produtos do banco têm maior probabilidade de possuir limites de crédito superiores.
7. Clientes com maior número de transações nos últimos 12 meses tendem a ter um limite de crédito mais alto.
8. Clientes com maior valor total de transações nos últimos 12 meses tendem a possuir limites de crédito mais elevados.
9. Clientes com menor número de meses inativos nos últimos 12 meses geralmente têm um limite de crédito mais alto.
10. Clientes com maior número de interações nos últimos 12 meses tendem a ter limites de crédito superiores.