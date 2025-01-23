```markdown
# Função para criar o pairplot
def criar_pairplot(coluna_principal, lista):
    # Adicionar colunas necessárias para o gráfico
    df['Customer_for'] = (pd.to_datetime('today') - pd.to_datetime(df['Dt_Customer'])).dt.days

    # Definir o tema e a paleta de cores
    sns.set_theme(rc={"axes.facecolor":"#FFF9ED","figure.facecolor":"#FFF9ED"})
    pallet = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"]

    # Selecionar as colunas para plotar
    To_Plot = lista + [coluna_principal, "Customer_for"]
    
    # Criar o pairplot
    plt.figure()
    sns.pairplot(df[To_Plot], hue=coluna_principal, palette="mako")
    
    # Mostrar o gráfico
    plt.show()

    df.drop(columns=['Customer_for'], inplace=True)

criar_pairplot('Education', ["Income", "Recency", "Age", "TotalMntSpent"])
```

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image.png)

```markdown
def strisce(titolo, textY, col, list_cols):
    # Definir faixas de idade automaticamente
    num_bins = 5  # Número de faixas de idade desejadas
    df['ColGroup'], bins = pd.qcut(df[col], q=num_bins, labels=False, retbins=True)

    labels = [f'{int(bins[i])}-{int(bins[i+1])}' for i in range(len(bins)-1)]
    df['ColGroup'] = pd.qcut(df[col], q=num_bins, labels=labels)

    # Agrupar os dados por faixa de idade e calcular a soma de crianças em cada faixa
    age_grouped = df.groupby('ColGroup')[list_cols].sum().reset_index()

    # Definir o estilo do gráfico
    sns.set(style="whitegrid")

    # Criar o gráfico de barras múltiplas
    plt.figure(figsize=(10, 6))
    age_grouped_melted = age_grouped.melt(id_vars='ColGroup', value_vars=list_cols, var_name='Colunas', value_name='Count')
    sns.barplot(data=age_grouped_melted, x='ColGroup', y='Count', hue='Colunas', palette="mako")

    # Adicionar título e rótulos aos eixos
    plt.title(f'{titolo}', fontsize=16)
    plt.xlabel(f'{col} (Faixas)', fontsize=14)
    plt.ylabel(f'{textY}', fontsize=14)

    # Mostrar o gráfico
    plt.show()

    df.drop(columns=['cat_income', 'ColGroup'], inplace=True)

strisce('Quantidade de Filhos por Faixa de Idade', 'Quantidade de Filhos', 
        'Income', ['Kidhome', 'Teenhome', 'Children'])
```

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image-1.png)

```markdown
def plot_distribution(column):
    plt.figure(figsize=(10, 6))
    
    if pd.api.types.is_numeric_dtype(df[column]):
        # Numeric data: Plot a histogram
        n, bins, patches = plt.hist(df[column], bins=20, color='blue', alpha=0.7, edgecolor='black')
        for i in range(len(patches)):
            patches[i].set_facecolor(sns.color_palette("rocket_r", as_cmap=True)(n[i] / max(n)))
            if n[i] > 0:
                plt.text(patches[i].get_x() + patches[i].get_width() / 2, n[i], int(n[i]), 
                         ha='center', va='bottom', fontsize=10, fontweight='bold')
        plt.title(f'Distribution of {column}', fontsize=16)
        plt.xlabel(column, fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
    
    else:
        # Categorical data: Plot a bar chart
        value_counts = df[column].value_counts()
        bars = plt.bar(value_counts.index, value_counts.values, color='blue', alpha=0.7, edgecolor='black')
        for i, bar in enumerate(bars):
            bar.set_facecolor(sns.color_palette("rocket_r", as_cmap=True)(value_counts.values[i] / max(value_counts.values)))
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), int(bar.get_height()), 
                     ha='center', va='bottom', fontsize=10, fontweight='bold')
        plt.title(f'Distribution of {column}', fontsize=16)
        plt.xlabel(column, fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

plot_distribution('Age')
plot_distribution('Education')
```

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image-2.png)

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image-3.png)

```markdown
def dispersion(col1, col2, hue=None):
    # Definir o estilo do gráfico
    sns.set(style="whitegrid")

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=col1, y=col2, hue=hue, palette='viridis', s=100)

    # Adicionar título e rótulos aos eixos
    plt.title(f'Relação entre {col1} & {col2}', fontsize=16)
    plt.xlabel(col1, fontsize=14)
    plt.ylabel(col2, fontsize=14)

    # Adicionar uma grade
    plt.grid(True)

    # Mostrar o gráfico
    plt.show()

dispersion('Income', 'TotalPurchases', 'Education')
dispersion('Income', 'TotalMntSpent')
```

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image-4.png)

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image-5.png)

```markdown
def plot_pie_chart(title, product_columns):
    # Sum of each product category
    total_spend = df[product_columns].sum()
    # Create a DataFrame for Plotly
    data = {
        'Category': product_columns,
        'Total': total_spend
    }
    # Plotly Donut Chart with labels outside
    fig = px.pie(data, 
                names='Category', 
                values='Total', 
                title=title,
                color_discrete_sequence=px.colors.sequential.Reds)
    # Adjust to make it a donut chart and set labels outside
    fig.update_traces(hole=0.4, textinfo='percent', textposition='outside', textfont_size=14)
    # Update title
    fig.update_layout(title_font_size=16)

    fig.show()

plot_pie_chart('Distribution of Purchases and Web Visits across Product Categories', 
               ['NumDealsPurchases', 'NumWebPurchases','NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth'])
```

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image-6.png)

```markdown
def timeline_comparison(titulo, text_x, var_name, operacao, columns):
    # Certifique-se de que a coluna 'Date' esteja no formato datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # Extraia o ano e o mês da coluna 'Date'
    df['YearMonth'] = df['Date'].dt.to_period('M')

    # Dicionário para mapear operações às funções do Pandas
    operacoes = {'sum': 'sum', 'mean': 'mean', 'median': 'median', 'std': 'std', 'var': 'var', 'max': 'max', 'min': 'min'}

    # Agrupe os dados por mês e aplique a operação especificada
    monthly_sales = df.groupby('YearMonth')[columns].agg(operacoes[operacao]).reset_index()
    # Converta 'YearMonth' para string para melhor visualização no gráfico
    monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)

    # Reorganize os dados para o Seaborn
    monthly_sales_melted = monthly_sales.melt(id_vars='YearMonth', 
                                              value_vars=columns,
                                              var_name=var_name, 
                                              value_name=text_x)
    # Defina o estilo do Seaborn
    sns.set(style='whitegrid')
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=monthly_sales_melted, x='YearMonth', y=text_x, hue=var_name, marker='o', linewidth=2.5)

    # Adicione título e rótulos
    plt.title(titulo, fontsize=18, fontweight='bold')
    plt.xlabel('Mês', fontsize=14)
    plt.ylabel(text_x, fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title=var_name, title_fontsize='13', fontsize='12')
    
    # Adicione uma grade de fundo
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()
    df.drop(columns='YearMonth', inplace=True)
```

![alt text](https://raw.githubusercontent.com/enzoschitini/Backup-Folder/refs/heads/CustomerPersonalityAnalysis/img/image-7.png)