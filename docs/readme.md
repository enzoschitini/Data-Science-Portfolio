
# Customer Personality Analysis
Analysis of company's ideal customers

## **Sobre o conjunto de dados**

### **Contexto**

**Declaração do problema**

A análise de personalidade do cliente é uma análise detalhada dos clientes ideais de uma empresa. Ela ajuda uma empresa a entender melhor seus clientes e facilita a modificação de produtos de acordo com as necessidades, comportamentos e preocupações específicas de diferentes tipos de clientes.

A análise de personalidade do cliente ajuda uma empresa a modificar seu produto com base em seus clientes-alvo de diferentes tipos de segmentos de clientes. Por exemplo, em vez de gastar dinheiro para comercializar um novo produto para cada cliente no banco de dados da empresa, uma empresa pode analisar qual segmento de clientes tem mais probabilidade de comprar o produto e, então, comercializá-lo apenas naquele segmento específico.

### **Conteúdo**

### **Tabela: Pessoas**
| **Coluna**        | **Descrição**                                                                         |
|-------------------|---------------------------------------------------------------------------------------|
| **ID**            | Identificador exclusivo do cliente.                                                  |
| **Ano_Nascimento**| Ano de nascimento do cliente.                                                        |
| **Educação**      | Nível de educação do cliente.                                                        |
| **Estado civil**  | Estado civil do cliente.                                                             |
| **Renda**         | Renda familiar anual do cliente.                                                     |
| **Kidhome**       | Número de crianças na casa do cliente.                                               |
| **Teenhome**      | Número de adolescentes na casa do cliente.                                           |
| **Dt_Cliente**    | Data de inscrição do cliente na empresa.                                             |
| **Ano**           | Ano da última compra do cliente.                                                     |
| **Mês**           | Mês da última compra do cliente.                                                     |
| **Dia**           | Dia da última compra do cliente.                                                     |
| **Idade**         | Idade do cliente, calculada a partir do ano de nascimento e da data de inscrição.     |
| **Recência**      | Número de dias desde a última compra do cliente.                                     |
| **Reclamação**    | Indica se o cliente reclamou nos últimos 2 anos (1 para sim, 0 para não).            |
| **Filhos**        | Número de filhos do cliente.                                                         |
| **TamanhoFamília**| Tamanho total da família do cliente, incluindo ele mesmo e seus dependentes.          |
| **EstáCasado**    | Indica se o cliente está casado (1 para sim, 0 para não).                            |
| **Senioridade**   | Número de dias desde que o cliente se inscreveu na empresa.                          |

### **Tabela: Produtos**
| **Coluna**          | **Descrição**                                                          |
|---------------------|----------------------------------------------------------------------|
| **MntWines**         | Valor gasto em vinho nos últimos 2 anos.                             |
| **MntFruits**        | Valor gasto em frutas nos últimos 2 anos.                            |
| **MntMeatProducts**  | Valor gasto em carne nos últimos 2 anos.                             |
| **MntFishProducts**  | Valor gasto em peixe nos últimos 2 anos.                             |
| **MntSweetProducts** | Valor gasto em doces nos últimos 2 anos.                             |
| **MntGoldProds**     | Valor gasto em ouro nos últimos 2 anos.                              |
| **TotalMntSpent**    | Total gasto em todos os produtos nos últimos 2 anos.                 |
| **TotalCompras**     | Total de compras feitas nos últimos 2 anos.                          |
| **ValorMédiaCompra** | Valor médio das compras feitas nos últimos 2 anos.                   |

### **Tabela: Promoção**
| **Coluna**            | **Descrição**                                                                  |
|-----------------------|-------------------------------------------------------------------------------|
| **NumDealsPurchases** | Número de compras feitas com desconto.                                       |
| **AcceptedCmp1**      | Indica se o cliente aceitou a oferta na 1ª campanha (1 para sim, 0 para não). |
| **AcceptedCmp2**      | Indica se o cliente aceitou a oferta na 2ª campanha (1 para sim, 0 para não). |
| **AcceptedCmp3**      | Indica se o cliente aceitou a oferta na 3ª campanha (1 para sim, 0 para não). |
| **AcceptedCmp4**      | Indica se o cliente aceitou a oferta na 4ª campanha (1 para sim, 0 para não). |
| **AcceptedCmp5**      | Indica se o cliente aceitou a oferta na 5ª campanha (1 para sim, 0 para não). |
| **Resposta**          | Indica se o cliente aceitou a oferta na última campanha (1 para sim, 0 para não).|

### **Tabela: Local**
| **Coluna**             | **Descrição**                                                   |
|------------------------|---------------------------------------------------------------|
| **NumWebPurchases**     | Número de compras feitas pelo site da empresa.               |
| **NumCatalogPurchases** | Número de compras feitas usando um catálogo.                 |
| **NumStorePurchases**   | Número de compras feitas diretamente em lojas.               |
| **NumWebVisitsMonth**   | Número de visitas ao site da empresa no último mês.          |
| **WebVsStorePurchases** | Relação entre compras feitas no site e em lojas físicas.     |


### **Alvo**

Precisa realizar clustering para resumir segmentos de clientes.

## Primeiras linhas do Dataset:

| ID   | Year_Birth | Education | Marital_Status | Income | Kidhome | Teenhome | Dt_Customer | Year | Month | Day | Age | Recency | Complain | Children | FamilySize | IsMarried | SeniorityDays | MntWines | MntFruits | MntMeatProducts | MntFishProducts | MntSweetProducts | MntGoldProds | TotalMntSpent | TotalPurchases | AvgPurchaseValue | NumDealsPurchases | AcceptedCmp1 | AcceptedCmp2 | AcceptedCmp3 | AcceptedCmp4 | AcceptedCmp5 | AcceptedAnyCampaign | Response | NumWebPurchases | NumCatalogPurchases | NumStorePurchases | NumWebVisitsMonth | WebVsStorePurchases |
|------|------------|-----------|----------------|--------|---------|----------|-------------|------|-------|-----|-----|---------|----------|----------|------------|-----------|---------------|----------|-----------|------------------|-----------------|------------------|--------------|---------------|----------------|------------------|-------------------|--------------|--------------|--------------|--------------|--------------|----------------------|----------|-----------------|--------------------|-------------------|------------------|---------------------|
| 5524 | 1957       | Graduation | Single         | 58138  | 0       | 0        | 2012-09-04  | 2012 | 9     | 4   | 57  | 58      | 0        | 0        | 0          | 0         | 663           | 635      | 88        | 546              | 172             | 88               | 88           | 1617          | 25             | 64               | 3                 | 0            | 0            | 0            | 0            | 0            | 1                    | 8        | 10              | 4                  | 7                 | 2                |
| 2174 | 1954       | Graduation | Single         | 46344  | 1       | 1        | 2014-03-08  | 2014 | 3     | 8   | 60  | 38      | 0        | 2        | 2          | 0         | 113           | 11       | 1         | 6                | 2               | 1                | 6            | 27           | 6              | 4                | 2                 | 0            | 0            | 0            | 0            | 0            | 0                    | 1        | 1               | 2                  | 5                 | 0                |
| 4141 | 1965       | Graduation | Together       | 71613  | 0       | 0        | 2013-08-21  | 2013 | 8     | 21  | 49  | 26      | 0        | 0        | 1          | 1         | 312           | 426      | 49        | 127              | 111             | 21               | 42           | 776           | 21             | 36               | 1                 | 0            | 0            | 0            | 0            | 0            | 0                    | 8        | 2               | 10                 | 4                 | 0                |
| 6182 | 1984       | Graduation | Together       | 26646  | 1       | 0        | 2014-02-10  | 2014 | 2     | 10  | 30  | 26      | 0        | 1        | 2          | 1         | 139           | 11       | 4         | 20               | 10              | 3                | 5            | 53           | 8              | 6                | 2                 | 0            | 0            | 0            | 0            | 0            | 0                    | 2        | 0               | 4                  | 6                 | 0                |
| 5324 | 1981       | PhD        | Married        | 58293  | 1       | 0        | 2014-01-19  | 2014 | 1     | 19  | 33  | 94      | 0        | 1        | 2          | 1         | 161           | 173      | 43        | 118              | 46              | 27               | 15           | 422           | 19             | 22               | 5                 | 0            | 0            | 0            | 0            | 0            | 0                    | 5        | 3               | 6                  | 5                 | 0                |


# **Links:**

[GitHub](https://github.com/enzoschitini/Backup-Folder/tree/CustomerPersonalityAnalysis)

[Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

[Customer Segmentation Clustering by Kevin](https://www.kaggle.com/code/kebinnuil/customer-segmentation-clustering-by-kevin)

[🛍 Customer Analysis| EDA | Profiling | KMeans](https://www.kaggle.com/code/visitnehaverma/customer-analysis-eda-profiling-kmeans)

[💼 Customer Personality Analysis: 🎯 Unsupervised](https://www.kaggle.com/code/sajjadalishah/customer-personality-analysis-unsupervised)

[Customer EDA | Clustering | Strategies](https://www.kaggle.com/code/marcelobatalhah/customer-eda-clustering-strategies)

[Clustering | Customer personality analysis](https://www.kaggle.com/code/a7madmostafa/clustering-customer-personality-analysis)

[market segmentation analysis](https://www.kaggle.com/code/taylorwill/market-segmentation-analysis)

[Customer Personality Analysis with Python | Thecleverprogrammer](https://thecleverprogrammer.com/2021/02/08/customer-personality-analysis-with-python/)

- Datasets
    
    [Customer Segmentation: Clustering 🛍️🛒🛒](https://www.kaggle.com/code/karnikakapoor/customer-segmentation-clustering)
    
    [Wine Dataset for Clustering](https://www.kaggle.com/datasets/harrywang/wine-dataset-for-clustering)
    
    [Credit Card Customer Data](https://www.kaggle.com/datasets/aryashah2k/credit-card-customer-data)
    
    [Household Electric Power Consumption](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set)
    
    [Mall Customers Segmentation](https://www.kaggle.com/datasets/abdallahwagih/mall-customers-segmentation)
    
    [Bank Customer Segmentation (1M+ Transactions)](https://www.kaggle.com/datasets/shivamb/bank-customer-segmentation)
    
    [Social Media Usage and Emotional Well-Being](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being)
    
    [Customer Clustering](https://www.kaggle.com/datasets/dev0914sharma/customer-clustering)
    
    [Fish species sampling data - legnth and weight](https://www.kaggle.com/datasets/taweilo/fish-species-sampling-weight-and-height-data)
    
    [Search | Kaggle](https://www.kaggle.com/search?q=clustering+dataset+in%3Adatasets)


# Correlação de Pearson

![alt text](<img/Correlação de Pearson-1.png>)


| **Feature 1**       | **Feature 2**       | **Descrição da Relação**                                              | **Nível de Correlação** |
|----------------------|---------------------|------------------------------------------------------------------------|--------------------------|
| MntWines            | TotalMntSpent      | **Gastos com vinhos contribuem significativamente para o total gasto.**   | Forte (+)               |
| MntMeatProducts     | TotalMntSpent      | Gastos com carnes contribuem significativamente para o total gasto.   | Forte (+)               |
| MntGoldProds        | TotalMntSpent      | Gastos com produtos de ouro impactam o total gasto.                   | Forte (+)               |
| AvgPurchaseValue    | TotalMntSpent      | A média de valor por compra está fortemente ligada ao total gasto.    | Forte (+)               |
| NumStorePurchases   | TotalPurchases     | Compras em loja compõem boa parte das compras totais.                 | Forte (+)               |
| Year_Birth          | Age                | Ano de nascimento está inversamente relacionado com a idade.          | Forte (-)               |
| FamilySize          | Children           | Tamanho da família está ligado ao número de filhos.                   | Forte (+)               |
| MntWines            | AvgPurchaseValue   | Pessoas que gastam mais com vinhos têm maior valor médio de compra.    | Moderada (+)            |
| TotalPurchases      | TotalMntSpent      | O número total de compras está relacionado com o total gasto.         | Moderada (+)            |
| NumCatalogPurchases | TotalPurchases     | Compras por catálogo influenciam as compras totais.                   | Moderada (+)            |
| NumWebPurchases     | TotalPurchases     | **Compras na web estão relacionadas ao total de compras.**                | Moderada (+)            |
| AcceptedCmp1        | Response           | **Aceitação da campanha 1 tem relação com a resposta geral.**             | Moderada (+)            |
| AcceptedCmp2        | Response           | **Aceitação da campanha 2 tem relação com a resposta geral.**             | Moderada (+)            |
| Recency             | TotalPurchases     | **Recência tem uma relação mais fraca com o número total de compras.**    | Fraca (-)               |
| Income              | TotalMntSpent      | **A renda influencia levemente o total gasto.**                          | Fraca (+)               |

### Notas
1. **Forte correlação:** Valores acima de 0.7 ou abaixo de -0.7.
2. **Correlação moderada:** Valores entre 0.4 e 0.7 (ou -0.4 a -0.7).
3. **Correlação fraca:** Valores abaixo de 0.4 (ou -0.4).

# Clusters:

### Model 01: [4 Components and 3 Clusters] ✅

![alt text](img/m1.png)

### Model 02: [10 Components and 3 Clusters]

![alt text](img/m2.png)

### Model 03: [10 Components and 4 Clusters]

![alt text](img/m3.png)

### Model 04: [10 Components and 2 Clusters]

![alt text](img/m4.png)

### Model 05: [4 Components and 4 Clusters] ✅

![alt text](img/m5.png)


<img src="https://media.licdn.com/dms/image/v2/D4D03AQGKyH2VYxJFNw/profile-displayphoto-shrink_200_200/B4DZR3AMiKHkAc-/0/1737163329100?e=1742428800&v=beta&t=g3jnt105dxEQvOyv2XAy6EJjviKfFrw1yH61s28JqYk" alt="capa" width="100">

## [Enzo Schitini](www.linkedin.com/in/enzoschitini)
### Data Scientist & Data Analyst • Senior Bubble Developer • SQL • Ux/Ui Design 
[*@ Scituffy Founder*](https://scituffy.bubbleapps.io/version-test/index/home)


### **Comparação dos Perfis**  
| **Características**          | **Melhores Clientes**              | **Piores Clientes**             |  
|-------------------------------|------------------------------------|---------------------------------|  
| **Idade**                     | 40 a 58 anos                      | Abaixo de 40 anos              |  
| **Renda**                     | $42.000 a $80.000                 | Menos de $42.000               |  
| **Filhos (Adolescentes)**     | Pelo menos 1                      | Nenhum                         |  
| **Filhos (Crianças)**         | Nenhum                            | 1 ou 2                         |  
| **Escolaridade**              | Mestrado ou PhD                   | Ensino básico ou médio         |  
| **Estado civil**              | Ficando, divorciado ou viúvo      | Solteiro ou casado             | 