# Analytics Templates

## Tabela Pessoa:

### **1. Análise Demográfica**

1. **Gráfico de Barras para Distribuição de Educação**
    - **Objetivo**: Mostrar a quantidade de clientes em cada nível de educação.
    - **Tipo de gráfico**: Gráfico de barras verticais.
    - **Insights esperados**: Identificar quais níveis de educação predominam entre os clientes.
2. **Gráfico de Pizza para Estado Civil**
    - **Objetivo**: Mostrar a proporção de clientes em cada estado civil.
    - **Tipo de gráfico**: Gráfico de pizza ou de rosca.
    - **Insights esperados**: Avaliar o perfil familiar dos clientes.
3. **Histograma para Idade dos Clientes**
    - **Objetivo**: Visualizar a distribuição da idade dos clientes.
    - **Tipo de gráfico**: Histograma, com faixas etárias agrupadas.
    - **Insights esperados**: Identificar concentrações em determinadas faixas etárias.
4. **Boxplot para Renda Familiar por Educação**
    - **Objetivo**: Analisar a distribuição da renda familiar com base no nível de educação.
    - **Tipo de gráfico**: Boxplot, com cada caixa representando um nível de educação.
    - **Insights esperados**: Observar padrões de renda relacionados à educação.

---

### **2. Análise de Família e Composição do Lar**

1. **Gráfico de Barras Empilhadas para Tamanho da Família por Estado Civil**
    - **Objetivo**: Mostrar como o tamanho da família varia entre diferentes estados civis.
    - **Tipo de gráfico**: Gráfico de barras empilhadas, com segmentos para o tamanho da família.
    - **Insights esperados**: Entender o impacto do estado civil no tamanho familiar.
2. **Gráfico de Dispersão para Número de Filhos vs. Tamanho da Família**
    - **Objetivo**: Relacionar o número de filhos ao tamanho total da família.
    - **Tipo de gráfico**: Gráfico de dispersão.
    - **Insights esperados**: Identificar padrões na composição familiar.
3. **Gráfico de Barras para Número de Crianças e Adolescentes no Lar**
    - **Objetivo**: Comparar a quantidade média de crianças (Kidhome) e adolescentes (Teenhome) por cliente.
    - **Tipo de gráfico**: Gráfico de barras lado a lado.
    - **Insights esperados**: Visualizar a presença de dependentes no lar.

---

### **3. Análise de Comportamento de Compra e Fidelidade**

1. **Gráfico de Linha para Recência e Senioridade**
    - **Objetivo**: Comparar o tempo de fidelidade (Senioridade) com o tempo desde a última compra (Recência).
    - **Tipo de gráfico**: Gráfico de linha ou dispersão.
    - **Insights esperados**: Determinar se clientes mais antigos tendem a ser mais ou menos ativos.
2. **Heatmap de Frequência de Compras por Ano e Mês**
    - **Objetivo**: Mostrar a sazonalidade das compras ao longo dos anos e meses.
    - **Tipo de gráfico**: Heatmap, com intensidade representando frequência de compras.
    - **Insights esperados**: Identificar picos de atividade de compras.
3. **Gráfico de Rosca para Reclamações de Clientes**
    - **Objetivo**: Mostrar a proporção de clientes que reclamaram nos últimos dois anos.
    - **Tipo de gráfico**: Gráfico de rosca.
    - **Insights esperados**: Avaliar o nível geral de insatisfação.

---

### **4. Segmentação e Análise Avançada**

1. **Clusterização Visual de Clientes por Idade e Renda**
    - **Objetivo**: Identificar grupos de clientes com perfis semelhantes (por exemplo, idade e renda).
    - **Tipo de gráfico**: Gráfico de dispersão ou análise de clusters.
    - **Insights esperados**: Criar personas baseadas em perfis demográficos.
2. **Gráfico de Radar para Perfis de Clientes**
    - **Objetivo**: Comparar atributos como Senioridade, TamanhoFamília, Recência e Reclamações para diferentes segmentos.
    - **Tipo de gráfico**: Gráfico de radar.
    - **Insights esperados**: Traçar perfis claros de clientes.
3. **Gráfico de Pareto para Reclamações por Categoria Demográfica**
    - **Objetivo**: Mostrar a distribuição de reclamações por estado civil, nível de educação ou faixa etária.
    - **Tipo de gráfico**: Gráfico de Pareto (barras com linha cumulativa).
    - **Insights esperados**: Identificar quais grupos têm maior probabilidade de reclamar.

---

### **5. Relacionamentos entre Variáveis**

1. **Gráfico de Correlação entre Renda, Idade e Recência**
    - **Objetivo**: Explorar como a renda familiar e a idade se relacionam com o tempo desde a última compra.
    - **Tipo de gráfico**: Heatmap de correlação ou gráfico de dispersão 3D.
    - **Insights esperados**: Identificar fatores que influenciam a atividade de compra.
2. **Gráfico de Bolhas para Idade, Renda e Tamanho da Família**
    - **Objetivo**: Relacionar idade e renda ao tamanho da família, com bolhas representando grupos de clientes.
    - **Tipo de gráfico**: Gráfico de bolhas.
    - **Insights esperados**: Destacar segmentos de alto ou baixo poder aquisitivo com famílias grandes.

---

## Tabela Produtos:

### **1. Análise Geral de Gastos por Categoria de Produto**

1. **Gráfico de Barras para Comparação de Gastos**
    - **Objetivo**: Comparar os valores totais gastos em cada categoria de produto (MntWines, MntFruits, etc.).
    - **Tipo de gráfico**: Gráfico de barras verticais ou horizontais.
    - **Insights esperados**: Identificar quais categorias de produtos recebem mais investimento dos clientes.
2. **Gráfico de Pizza para Proporção de Gastos**
    - **Objetivo**: Mostrar a proporção do total gasto em cada categoria em relação ao gasto total (TotalMntSpent).
    - **Tipo de gráfico**: Gráfico de pizza ou de rosca.
    - **Insights esperados**: Identificar categorias que dominam os gastos.
3. **Gráfico de Radar para Perfil de Gastos**
    - **Objetivo**: Comparar os gastos de diferentes categorias para traçar o perfil de consumo.
    - **Tipo de gráfico**: Gráfico de radar, com cada eixo representando uma categoria de produto.
    - **Insights esperados**: Visualizar padrões gerais de consumo.

---

### **2. Análise de Compras e Valor Médio**

1. **Gráfico de Linha para Tendência de Valor Médio**
    - **Objetivo**: Analisar como o valor médio das compras (ValorMédiaCompra) varia ao longo do tempo ou por cliente.
    - **Tipo de gráfico**: Gráfico de linha.
    - **Insights esperados**: Avaliar consistência ou variações no ticket médio.
2. **Gráfico de Dispersão para Gastos Totais vs. Número de Compras**
    - **Objetivo**: Relacionar TotalMntSpent com TotalCompras.
    - **Tipo de gráfico**: Gráfico de dispersão, com cada ponto representando um cliente.
    - **Insights esperados**: Identificar clientes com alta frequência de compra versus aqueles que gastam mais em poucas compras.

---

### **3. Comparação de Categorias e Análise Avançada**

1. **Gráfico de Barras Empilhadas por Categoria de Produto**
    - **Objetivo**: Mostrar o total gasto por diferentes categorias em comparação com o total de compras.
    - **Tipo de gráfico**: Barras empilhadas, com cada segmento representando uma categoria.
    - **Insights esperados**: Identificar quais categorias são mais representativas em termos de gastos acumulados.
2. **Boxplot de Gastos por Categoria**
    - **Objetivo**: Mostrar a distribuição de gastos em cada categoria para identificar padrões e outliers.
    - **Tipo de gráfico**: Boxplot, com uma caixa para cada categoria.
    - **Insights esperados**: Verificar variabilidade e possíveis outliers.
3. **Gráfico de Calor para Correlação entre Categorias de Gastos**
    - **Objetivo**: Explorar a relação entre gastos em diferentes categorias.
    - **Tipo de gráfico**: Heatmap de correlação.
    - **Insights esperados**: Determinar se clientes que gastam mais em uma categoria tendem a gastar em outras.

---

### **4. Segmentação de Clientes com Base em Gastos**

1. **Clusterização Visual com Categorias de Produto**
    - **Objetivo**: Identificar grupos de clientes com base em seus padrões de gastos (MntWines, MntFruits, etc.).
    - **Tipo de gráfico**: Gráfico de dispersão 3D ou clusterização (como K-means).
    - **Insights esperados**: Descobrir segmentos de clientes, como "focados em vinhos" ou "multicategorias".
2. **Gráfico de Pareto (80/20)**
    - **Objetivo**: Mostrar as categorias de produtos que representam 80% dos gastos totais.
    - **Tipo de gráfico**: Gráfico de Pareto (barras com linha cumulativa).
    - **Insights esperados**: Identificar os produtos mais relevantes para o faturamento.

---

### **5. Exploração de Relações e Tendências**

1. **Gráfico de Bolhas para Gastos Médios por Produto e Total de Compras**
    - **Objetivo**: Relacionar TotalMntSpent, ValorMédiaCompra e TotalCompras.
    - **Tipo de gráfico**: Gráfico de bolhas, com tamanho das bolhas representando o valor médio das compras.
    - **Insights esperados**: Identificar clientes que combinam alta frequência de compras com alto ticket médio.
2. **Gráfico de Linha por Categoria para Evolução de Gastos**
    - **Objetivo**: Visualizar como os gastos em diferentes categorias evoluem ao longo do tempo (se disponível).
    - **Tipo de gráfico**: Gráfico de linha com uma linha para cada categoria.
    - **Insights esperados**: Identificar sazonalidade ou tendências de preferência.
3. **Histograma de Distribuição de Gastos Totais**
    - **Objetivo**: Mostrar a distribuição de TotalMntSpent entre os clientes.
    - **Tipo de gráfico**: Histograma.
    - **Insights esperados**: Identificar concentração de clientes em diferentes faixas de gasto.

---

## Tabela Campanhas:

### **1. Gráficos Focados em Aceitação de Campanhas**

1. **Gráfico de Colunas Empilhadas por Taxa de Aceitação**
    - **Objetivo**: Comparar a taxa de aceitação (1s) e rejeição (0s) para cada campanha (AcceptedCmp1 a Resposta).
    - **Tipo de gráfico**: Gráfico de colunas empilhadas, com segmentos para aceitação e rejeição.
    - **Insights esperados**: Visualizar o equilíbrio entre clientes que aceitaram e rejeitaram cada campanha.
2. **Gráfico de Radar para Engajamento de Campanhas**
    - **Objetivo**: Mostrar o engajamento total (soma de 1s) para cada campanha de forma radial.
    - **Tipo de gráfico**: Gráfico de radar, com cada eixo representando uma campanha.
    - **Insights esperados**: Identificar campanhas mais aceitas em um formato visual diferenciado.

---

### **2. Gráficos Relacionados a Compras com Desconto**

1. **Gráfico de Barras Agrupadas para Comparar Campanhas e Descontos**
    - **Objetivo**: Mostrar a média de compras com desconto (NumDealsPurchases) para clientes que aceitaram e rejeitaram campanhas.
    - **Tipo de gráfico**: Barras agrupadas por aceitação (sim/não) para cada campanha.
    - **Insights esperados**: Avaliar se quem aceita campanhas utiliza mais descontos.
2. **Gráfico de Linha por Segmento de Descontos**
    - **Objetivo**: Analisar a tendência de aceitação das campanhas com base em faixas de compras com desconto (baixo, médio, alto).
    - **Tipo de gráfico**: Gráfico de linha, com linhas separadas por segmento de desconto.
    - **Insights esperados**: Observar se clientes que utilizam mais descontos respondem melhor às campanhas.

---

### **3. Gráficos Relacionados à Interação entre Variáveis**

1. **Matriz de Contagem entre Aceitação de Campanhas**
    - **Objetivo**: Mostrar quantos clientes aceitaram combinações específicas de campanhas.
    - **Tipo de gráfico**: Heatmap, com AcceptedCmp1 a AcceptedCmp5 e Resposta como eixos.
    - **Insights esperados**: Identificar padrões de comportamento, como aceitar campanhas consecutivas.
2. **Gráfico de Bolhas para Relação entre Aceitação e Compras**
    - **Objetivo**: Representar a relação entre o número de campanhas aceitas, compras com desconto e aceitação da última campanha (Resposta).
    - **Tipo de gráfico**: Gráfico de bolhas, com o tamanho das bolhas representando o número de compras com desconto.
    - **Insights esperados**: Identificar clientes com alto engajamento e uso de descontos.
3. **Gráfico de Áreas Empilhadas para Taxa de Aceitação ao Longo do Tempo**
    - **Objetivo**: Visualizar a evolução da aceitação de campanhas segmentada por status (aceitou/não).
    - **Tipo de gráfico**: Gráfico de áreas empilhadas, com tempo ou sequência de campanhas no eixo X.
    - **Insights esperados**: Avaliar se o interesse pelos clientes aumentou ou diminuiu ao longo das campanhas.

---

### **4. Gráficos Avançados para Segmentação e Perfis**

1. **Clusterização Visual de Clientes**
    - **Objetivo**: Identificar grupos de clientes com base em campanhas aceitas e compras com desconto.
    - **Tipo de gráfico**: Gráfico de dispersão 3D ou gráfico de clusterização (como K-means).
    - **Insights esperados**: Descobrir segmentos de clientes que respondem de maneira similar às campanhas.
2. **Gráfico Sankey para Fluxo de Aceitação**
    - **Objetivo**: Visualizar o fluxo de aceitação ou rejeição em cada campanha.
    - **Tipo de gráfico**: Gráfico de Sankey, mostrando o caminho dos clientes através das campanhas.
    - **Insights esperados**: Identificar em que ponto os clientes "desistem" das campanhas.

---

### **5. Gráficos Explorando Outras Dinâmicas**

1. **Histograma de Distribuição de Compras com Desconto**
    - **Objetivo**: Analisar a distribuição do número de compras com desconto (NumDealsPurchases).
    - **Tipo de gráfico**: Histograma.
    - **Insights esperados**: Verificar se há concentração em determinados intervalos.
2. **Gráfico de Rosca para Comportamento de Resposta Final**
    - **Objetivo**: Mostrar a proporção de clientes que aceitaram ou rejeitaram a última campanha (Resposta).
    - **Tipo de gráfico**: Gráfico de rosca (uma variação do gráfico de pizza).
    - **Insights esperados**: Avaliar rapidamente o sucesso da última campanha.
3. **Gráfico de Cascata para Impacto de Descontos na Aceitação**
    - **Objetivo**: Mostrar como as compras com desconto (NumDealsPurchases) impactam a aceitação ao longo das campanhas.
    - **Tipo de gráfico**: Gráfico de cascata.
    - **Insights esperados**: Entender a contribuição incremental dos descontos para a aceitação.

---

1. **Gráfico de Barras para Aceitação de Campanhas**
    - **Objetivo**: Comparar a taxa de aceitação de cada campanha (AcceptedCmp1 a AcceptedCmp5 e Resposta).
    - **Tipo de gráfico**: Gráfico de barras horizontais, com a proporção de aceitação (percentual de 1s) para cada campanha.
    - **Insights esperados**: Identificar quais campanhas foram mais eficazes.
2. **Gráfico de Linhas para Tendência de Aceitação**
    - **Objetivo**: Visualizar a evolução da aceitação ao longo das campanhas.
    - **Tipo de gráfico**: Gráfico de linhas, com cada ponto representando a taxa de aceitação de uma campanha.
    - **Insights esperados**: Observar tendências de engajamento dos clientes ao longo do tempo.
3. **Heatmap para Correlação entre Campanhas**
    - **Objetivo**: Identificar a relação entre a aceitação das campanhas (AcceptedCmp1 a Resposta).
    - **Tipo de gráfico**: Heatmap de correlação entre as colunas binárias.
    - **Insights esperados**: Determinar se clientes que aceitaram uma campanha têm maior probabilidade de aceitar outras.
4. **Gráfico de Pizza para Compras com Desconto**
    - **Objetivo**: Mostrar a proporção de compras feitas com e sem desconto (NumDealsPurchases).
    - **Tipo de gráfico**: Gráfico de pizza, segmentando os clientes com base no número de compras com desconto.
    - **Insights esperados**: Avaliar a popularidade das ofertas com desconto.
5. **Boxplot para Análise de Descontos por Aceitação de Campanhas**
    - **Objetivo**: Examinar a distribuição de compras com desconto (NumDealsPurchases) por aceitação de campanhas (AcceptedCmpX).
    - **Tipo de gráfico**: Boxplot, com cada coluna representando uma campanha.
    - **Insights esperados**: Entender se aceitar campanhas está relacionado a maior uso de descontos.
6. **Gráfico de Dispersão para Análise de Aceitação e Compras**
    - **Objetivo**: Explorar a relação entre o número de compras feitas com desconto (NumDealsPurchases) e aceitação da última campanha (Resposta).
    - **Tipo de gráfico**: Gráfico de dispersão, com NumDealsPurchases no eixo Y e Resposta no eixo X (0 ou 1).
    - **Insights esperados**: Avaliar se quem aceita a última campanha tende a usar mais descontos.
7. **Gráfico de Barras Empilhadas para Comparação de Campanhas**
    - **Objetivo**: Comparar as taxas de aceitação em cada campanha com base no uso de descontos.
    - **Tipo de gráfico**: Gráfico de barras empilhadas, com uma barra para cada campanha segmentada pelo uso de descontos (baixo, médio, alto).
    - **Insights esperados**: Determinar se o uso de descontos influencia a aceitação de ofertas.

---

## Tabela Local:

1. **Gráfico de Barras para Análise Comparativa**  
   - **Objetivo**: Comparar os valores médios ou totais das colunas relacionadas às compras (NumWebPurchases, NumCatalogPurchases, NumStorePurchases).  
   - **Tipo de gráfico**: Gráfico de barras agrupadas, com cada barra representando o total de compras por método.  
   - **Insights esperados**: Identificar o canal de vendas mais utilizado pelos clientes.

2. **Gráfico de Linha para Tendências de Visitas ao Site**  
   - **Objetivo**: Analisar como o número de visitas ao site (NumWebVisitsMonth) se relaciona com as compras online (NumWebPurchases).  
   - **Tipo de gráfico**: Gráfico de linha com duas séries: uma representando visitas ao site e outra representando compras online.  
   - **Insights esperados**: Entender se há uma relação direta entre visitas e conversões.

3. **Gráfico de Dispersão com Relação Web vs. Loja**  
   - **Objetivo**: Explorar a relação entre compras no site e em lojas físicas (WebVsStorePurchases).  
   - **Tipo de gráfico**: Gráfico de dispersão, com WebVsStorePurchases no eixo Y e o total de compras no eixo X.  
   - **Insights esperados**: Avaliar o equilíbrio entre os dois canais.

4. **Gráfico de Pizza para Análise de Proporção**  
   - **Objetivo**: Mostrar a proporção de compras realizadas por diferentes canais (site, catálogo, lojas).  
   - **Tipo de gráfico**: Gráfico de pizza.  
   - **Insights esperados**: Identificar a contribuição relativa de cada canal.

5. **Boxplot para Distribuição de Compras**  
   - **Objetivo**: Avaliar a distribuição e identificar padrões ou outliers nas compras por canal (NumWebPurchases, NumCatalogPurchases, NumStorePurchases).  
   - **Tipo de gráfico**: Boxplot para cada canal.  
   - **Insights esperados**: Detectar variações extremas no comportamento de compra.

6. **Gráfico de Área para Evolução de Visitas e Compras**  
   - **Objetivo**: Demonstrar a relação acumulada entre visitas ao site (NumWebVisitsMonth) e compras online ao longo do tempo.  
   - **Tipo de gráfico**: Gráfico de área empilhada.  
   - **Insights esperados**: Avaliar se há um crescimento sincronizado entre as visitas e as compras.











	ID	Education	Marital_Status	Income	Age	Recency	Complain	FamilySize	IsMarried	Date
0	5524	Graduation	Single	58138	57	58	0	0	0	2012-09-04
1	2174	Graduation	Single	46344	60	38	0	2	0	2014-03-08
2	4141	Graduation	Together	71613	49	26	0	1	1	2013-08-21
3	6182	Graduation	Together	26646	30	26	0	2	1	2014-02-10
4	5324	PhD	Married	58293	33	94	0	2	1	2014-01-19
