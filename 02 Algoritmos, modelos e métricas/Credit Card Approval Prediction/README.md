# 💳 Previsão de Risco de Inadimplência em Cartões de Crédito: 

<img src="https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/main/02%20Algoritmos%2C%20modelos%20e%20m%C3%A9tricas/Credit%20Card%20Approval%20Prediction/image/ML%20Credit%20Card%20Score%20Model.png">

---

# **Machine Learning** • Credit Card Approval Prediction

Bem-vindo(a)!!! Meu nome é Enzo Schitini, sou cientista de dados e neste projeto de "Previsão de Aprovação de Cartão de Crédito", utilizamos técnicas de machine learning para desenvolver um modelo capaz de prever a aprovação ou rejeição de solicitações de cartão de crédito. Analisamos dados históricos de clientes, incluindo informações demográficas e financeiras, para identificar padrões que influenciam a decisão de aprovação. 

Nosso objetivo é fornecer às instituições financeiras uma ferramenta precisa para minimizar riscos de crédito e otimizar o processo de concessão, assegurando que apenas clientes qualificados sejam aprovados.

**Data Science** Portfólio | *22 Agosto 2024* - *04 Setembro 2024*

[Enzo Schitini](https://www.linkedin.com/in/enzoschitini/) - Data Scientist & Data Analyst • Expert Bubble.io • UX & UI @ Scituffy creator

---

## O que você vai encontrar neste notebook? 👋

Este projeto visa desenvolver um modelo de machine learning capaz de prever a aprovação de crédito para novos clientes de um banco. A análise se concentrará em dados demográficos, financeiros e de comportamento de clientes existentes, com o objetivo de identificar padrões que podem ser utilizados para otimizar o processo de concessão de crédito.

O processo de aprovação de crédito é crucial para qualquer instituição financeira, pois impacta diretamente a lucratividade e o risco do negócio. No entanto, o volume crescente de solicitações exige métodos eficientes para analisar e classificar os candidatos. É nesse contexto que a análise de dados e o machine learning surgem como ferramentas poderosas para automatizar e melhorar a tomada de decisão.

#### Os pilares da análise:
A análise se concentrará em três pilares principais para extrair insights relevantes e construir um modelo preditivo eficaz:

1. **🎯 Entender como é o perfil dos clentes desse banco**
2. **🎯 Quais características dos clientes são mais propensas a resultar em default?**
3. **🎯 Criar um modelo de Machine Learning para fazer previsões**

#### - *Metodologia*

A análise será conduzida utilizando técnicas estatísticas e de visualização de dados para identificar padrões e anomalias. Será empregado o Python como ferramentas de manipulação e análise dos dados, na limpeza e preparação dos dados para garantir a qualidade das análises e do modelo de Machine Learning.

**Importância do Projeto:**

A implementação de um modelo preditivo para aprovação de crédito oferece diversos benefícios ao banco, incluindo:

- **Redução de riscos:** Identificação de clientes de alto risco para evitar concessões de crédito que possam resultar em inadimplência.
- **Aumento da lucratividade:** Aprovação de clientes com alta probabilidade de pagamento, ampliando o volume de crédito concedido.
- **Melhoria da experiência do cliente:** Agilização do processo de aprovação e oferta de soluções personalizadas aos clientes.
- **Otimização de recursos:** Direcionamento estratégico dos esforços de marketing e vendas para clientes com maior chance de aprovação.

# Colunas do csv

| **1. Variáveis Demográficas**       | **2. Variáveis Financeiras**     | **3. Variáveis de Tempo**      | **4. Variáveis do Cartão**     | **5. Variável de Default** |
|-------------------------------------|----------------------------------|--------------------------------|--------------------------------|----------------------------|
| id                                  | salario_anual                    | meses_de_relacionamento        | tipo_cartao                    | default                    |
| idade                               | limite_credito                   | interacoes_12m                 | taxa_utilizacao_credito        |                            |
| sexo                                | renda_alta                       | meses_inativo_12m              | valor_medio_transacao          |                            |
| dependentes                         |                                  | valor_transacoes_12m           | frequencia_interacao           |                            |
| escolaridade                        |                                  | qtd_transacoes_12m             | qtd_produtos                   |                            |
| estado_civil                        |                                  | transacoes_por_mes             |                                |                            |
| grupo_etario                        |                                  | meses_ativos_12m               |                                |                            |
| idade_faixa                         |                                  |                                |                                |                            |
| idade_estado_civil                  |                                  |                                |                                |                            |
| escolaridade_renda                  |                                  |                                |                                |                            |

# Descrição:

| **Coluna**                    | **Descrição**                                                                 |
|-------------------------------|------------------------------------------------------------------------------|
| **ID**                        | Identificador exclusivo de cada cliente.                                      |
| **Idade**                     | Anos de vida do cliente.                                                      |
| **Sexo**                      | Gênero do cliente, codificado como "M" para Masculino e "F" para Feminino. |
| **Dependentes**               | Quantidade de dependentes do cliente.                                         |
| **Escolaridade**              | Nível educacional alcançado pelo cliente.                                     |
| **Estado Civil**              | Condição marital do cliente.                                                  |
| **Grupo Etário**              | Faixa etária do cliente, categorizada em grupos como "Adulto", "Idoso", etc. |
| **Idade Faixa**               | Faixa específica de idade do cliente, como "38-45", "46-51", etc.             |
| **Idade Estado Civil**        | Combinação da idade e estado civil do cliente, por exemplo, "45 - casado".    |
| **Escolaridade Renda**        | Combinação do nível de escolaridade e faixa de renda anual do cliente, como "ensino médio - $60K - $80K". |
| **Salário Anual**             | Faixa de renda anual estimada do cliente, como "menos que $40K", "$60K - $80K", etc. |
| **Limite de Crédito**         | Montante de crédito disponível ao cliente.                                    |
| **Renda Alta**                | Indicador binário (0 ou 1). |
| **Meses de Relacionamento**   | Duração do relacionamento do cliente com a instituição financeira em meses.   |
| **Interações 12m**            | Número de interações do cliente com a instituição financeira nos últimos 12 meses. |
| **Meses Inativo 12m**         | Quantidade de meses que o cliente esteve inativo nos últimos 12 meses.        |
| **Valor Transações 12m**      | Valor total das transações do cliente nos últimos 12 meses.                   |
| **Qtd Transações 12m**        | Número total de transações realizadas pelo cliente nos últimos 12 meses.      |
| **Transações por Mês**        | Média mensal de transações do cliente nos últimos 12 meses.                   |
| **Meses Ativos 12m**          | Número de meses em que o cliente esteve ativo nos últimos 12 meses.           |
| **Tipo Cartão**               | Tipo de cartão de crédito do cliente, como "blue", "gold", etc.               |
| **Taxa Utilização Crédito**   | Percentual do limite de crédito utilizado pelo cliente.                       |
| **Valor Médio Transação**     | Média do valor das transações do cliente nos últimos 12 meses.                |
| **Frequência Interação**      | Frequência de interações do cliente com a instituição financeira nos últimos 12 meses. |
| **Qtd Produtos**              | Número de produtos financeiros que o cliente possui na instituição.           |
| **Default**                   | Indicador binário (0 ou 1), que mostra se o cliente está inadimplente ou não. |

# 🎯 Insights

<img src="https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/main/02%20Algoritmos%2C%20modelos%20e%20m%C3%A9tricas/Credit%20Card%20Approval%20Prediction/image/An%C3%A1lise%20descritiva%20e%20Insights.png">

###
# Gráfico de dispersão do Default

<img src="https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/main/02%20Algoritmos%2C%20modelos%20e%20m%C3%A9tricas/Credit%20Card%20Approval%20Prediction/image/Gr%C3%A1fico%20de%20dispers%C3%A3o%20do%20Default.png">

###
# Análise de Dados para Modelo de Credit Score: Relação com Default


## Quais padrões comportamentais são indicadores de risco de default?

1. **Perfil do Cliente:**
   - **Idade:** Jovens podem apresentar maior propensão à inadimplência.
   - **Sexo:** Avaliar diferenças de inadimplência entre homens e mulheres.
   - **Dependentes:** Mais dependentes podem aumentar a necessidade de crédito e os desafios para honrar dívidas.
   - **Escolaridade:** Pode influenciar o conhecimento financeiro e capacidade de gerenciamento de dívidas.
   - **Estado Civil:** Impacta a renda familiar e responsabilidades financeiras.
   - **Grupo Etário:** Analisar o comportamento de pagamento de diferentes faixas etárias.
   - **Salário Anual:** Renda é um fator fundamental na avaliação de risco de crédito.
   - **Renda Alta:** Investigar se clientes com renda alta têm menor probabilidade de inadimplência.

2. **Histórico de Crédito:**
   - **Limite de Crédito:** Um limite alto pode indicar maior confiança no cliente, mas também aumentar o risco de inadimplência.
   - **Meses de Relacionamento:** Indica fidelidade e responsabilidade.
   - **Interações nos últimos 12 meses:** Número de interações como indicador de engajamento.
   - **Meses Inativos nos últimos 12 meses:** Períodos de inatividade podem indicar dificuldades financeiras e maior risco.

3. **Padrões de Gastos:**
   - **Valor das Transações nos últimos 12 meses:** Reflete a capacidade de pagamento do cliente.
   - **Quantidade de Transações nos últimos 12 meses:** Frequência de compras como indicador de consumo impulsivo ou dificuldades financeiras.
   - **Transações por Mês:** Analisar variações de gastos ao longo do ano.
   - **Meses Ativos nos últimos 12 meses:** Frequência de uso e risco de inadimplência.
   - **Tipo de Cartão:** Diferentes tipos de cartão impactam o comportamento de pagamento.
   - **Taxa de Utilização do Crédito:** Nível de endividamento em relação ao limite disponível.
   - **Valor Médio da Transação:** Indica o perfil de consumo do cliente.
   - **Frequência de Interação:** Frequência de contato com a instituição como indicador de necessidades de suporte.
   - **Quantidade de Produtos:** Número de produtos contratados como indicador de fidelidade e relacionamento.

**Objetivo:** Analisar a relação entre as características dos clientes e a probabilidade de default, com o intuito de aprimorar o modelo de credit score e reduzir o risco de crédito.


# 🎯 Machine Learning

<img src="https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/main/02%20Algoritmos%2C%20modelos%20e%20m%C3%A9tricas/Credit%20Card%20Approval%20Prediction/image/Credit%20Card%20Approval%20Prediction.png">

---

# **Machine Learning** • Credit Card Approval Prediction

Para o desenvolvimento deste projeto, a próxima etapa envolve a escolha e aplicação de um modelo de Machine Learning adequado para prever o risco de inadimplência em cartões de crédito. A escolha do modelo depende de vários fatores, como a natureza dos dados, a complexidade desejada, e a necessidade de interpretabilidade.

### O modelo construído permitirá:

**Classificação de clientes por risco:** Categorizar clientes conforme a probabilidade de inadimplência, possibilitando que instituições financeiras direcionem estratégias específicas para cada grupo.

**Previsão da inadimplência:** Estimar a probabilidade de um cliente específico se tornar inadimplente, auxiliando nas decisões sobre concessão de crédito e definição de limites.

**Identificação dos principais fatores de risco:** Análise exploratória para revelar as características dos clientes e seus padrões de consumo mais fortemente associados à inadimplência.

---

<img src="https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/main/02%20Algoritmos%2C%20modelos%20e%20m%C3%A9tricas/Credit%20Card%20Approval%20Prediction/image/Classification%20Report.png">

Os resultados apresentados indicam um bom desempenho do modelo de classificação na tarefa de prever a inadimplência em cartões de crédito. Vamos analisar as métricas:

Aqui estão os resultados organizados em uma tabela:

|               | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| **Classe 0**  | 0.97      | 0.95   | 0.96     | 1185    |
| **Classe 1**  | 0.79      | 0.87   | 0.83     | 232     |
| **Accuracy**  |           |        | 0.94     | 1417    |
| **Macro Avg** | 0.88      | 0.91   | 0.89     | 1417    |
| **Weighted Avg** | 0.94  | 0.94   | 0.94     | 1417    |

- **Precision**: A precisão para a classe 0 (não inadimplente) é de 0.97, enquanto para a classe 1 (inadimplente) é de 0.79. Isso significa que 97% das previsões de não inadimplência estão corretas, mas a precisão para inadimplentes é um pouco menor, com 79% das previsões corretas. A diferença na precisão entre as classes pode indicar um desequilíbrio entre as classes no conjunto de dados ou que o modelo tem dificuldade em identificar corretamente os inadimplentes.

- **Recall**: O recall para a classe 0 é de 0.95, o que indica que 95% dos casos de não inadimplência foram corretamente identificados. Para a classe 1, o recall é de 0.87, indicando que 87% dos casos de inadimplência foram corretamente identificados. Isso mostra que o modelo é razoavelmente bom em capturar a maioria dos casos de inadimplência, apesar de não atingir o mesmo nível de recall da classe 0.

- **F1-score**: O F1-score combina a precisão e o recall em uma única métrica, sendo útil especialmente quando há um desbalanceamento entre as classes. Para a classe 0, o F1-score é de 0.96, e para a classe 1 é de 0.83. Um F1-score de 0.83 para inadimplentes é relativamente bom, mas ainda existe espaço para melhoria, especialmente considerando a importância de prever corretamente casos de inadimplência.

- **Accuracy**: A acurácia geral do modelo é de 0.94, indicando que 94% das previsões totais foram corretas. Isso sugere que o modelo está funcionando bem em geral, mas a acurácia pode ser um pouco enganosa em casos de classes desbalanceadas.

- **Macro avg e Weighted avg**: A média macro (macro avg) e a média ponderada (weighted avg) das métricas mostram que, mesmo considerando as diferenças no número de exemplos por classe, o modelo mantém uma performance equilibrada, com valores próximos para precisão, recall, e F1-score.

**Interpretação Geral**: O modelo mostra um excelente desempenho na previsão de clientes que não vão se tornar inadimplentes (classe 0), mas é ligeiramente menos eficaz na previsão daqueles que vão se tornar inadimplentes (classe 1). Isso pode ser aceitável dependendo do contexto e das implicações de cada tipo de erro. Se a identificação correta de inadimplentes for crucial, pode ser necessário ajustar o modelo ou explorar técnicas como o balanceamento de classes para melhorar o recall e a precisão da classe 1.
