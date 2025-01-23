Per analizzare questi dati finanziari, ci sono diverse metriche utili che possiamo calcolare e visualizzare. Ecco alcune delle principali:

### 1. **Statistiche Descrittive**

- **Media**: La media dei prezzi (apertura, chiusura, alta, bassa).
- **Mediana**: Il valore mediano dei prezzi.
- **Deviazione standard**: Per misurare la volatilità.
- **Varianza**: Per misurare la dispersione dei dati.

### 2. **Analisi di Trend**

- **Media mobile**: Calcolare le medie mobili a 7, 14, e 30 giorni per identificare i trend.
- **Indice di Forza Relativa (RSI)**: Per valutare se il titolo è ipercomprato o ipervenduto.
- **MACD (Moving Average Convergence Divergence)**: Per identificare le tendenze di prezzo.

### 3. **Analisi della Volatilità**

- **Range giornaliero**: Differenza tra il prezzo massimo e minimo ogni giorno.
- **ATR (Average True Range)**: Misura della volatilità.

### 4. **Analisi del Volume**

- **Volume medio**: Il volume medio delle transazioni su un periodo di tempo.
- **Volume relativo**: Volume di un giorno specifico rispetto alla media.

### 5. **Analisi dei Ritorni**

- **Ritorno giornaliero**: Percentuale di variazione del prezzo di chiusura giorno per giorno.
- **Ritorno cumulativo**: Ritorno totale nel periodo di tempo considerato.

### 6. **Correlazioni**

- **Correlazione tra volume e prezzo**: Per vedere se c'è una relazione tra il volume degli scambi e i movimenti di prezzo.

### 7. **Indicatori Tecnici**

- **Bollinger Bands**: Per misurare l'alta e bassa volatilità di un titolo rispetto ai precedenti movimenti di prezzo.
- **Supporto e Resistenza**: Livelli di prezzo che agiscono come barriera al movimento del prezzo.

Ecco come potremmo iniziare con alcune di queste analisi:

1. **Statistiche Descrittive**: Calcolare la media, mediana, deviazione standard e varianza per le colonne dei prezzi.
2. **Analisi di Trend**: Calcolare e tracciare le medie mobili.
3. **Analisi della Volatilità**: Calcolare e tracciare l'ATR.
4. **Analisi del Volume**: Calcolare e tracciare il volume medio e relativo.

Iniziamo calcolando alcune statistiche descrittive e creando le medie mobili per visualizzare i trend.

### Calcoli delle Metriche

### 1. Statistiche Descrittive

```python
pythonCopia codice
# Statistiche descrittive
stats = df.describe()
stats
```

### 2. Medie Mobili

```python
pythonCopia codice
# Medie mobili
df['MA7'] = df['Fechamento'].rolling(window=7).mean()
df['MA14'] = df['Fechamento'].rolling(window=14).mean()
df['MA30'] = df['Fechamento'].rolling(window=30).mean()
```

### 3. Ritorni Giornalieri

```python
pythonCopia codice
# Calcolo dei ritorni giornalieri
df['Ritorno Giornaliero'] = df['Fechamento'].pct_change()
```

### 4. ATR (Average True Range)

```python
pythonCopia codice
# Calcolo dell'ATR
df['TR'] = df[['Alta', 'Baixa', 'Fechamento']].apply(lambda x: max(x['Alta'] - x['Baixa'], abs(x['Alta'] - x['Fechamento']), abs(x['Baixa'] - x['Fechamento'])), axis=1)
df['ATR'] = df['TR'].rolling(window=14).mean()
```

### Visualizzazione delle Medie Mobili e dell'ATR

```python
pythonCopia codice
import matplotlib.pyplot as plt

plt.figure(figsize=(14,7))
plt.plot(df['Data'], df['Fechamento'], label='Fechamento')
plt.plot(df['Data'], df['MA7'], label='MA 7 Giorni')
plt.plot(df['Data'], df['MA14'], label='MA 14 Giorni')
plt.plot(df['Data'], df['MA30'], label='MA 30 Giorni')
plt.xlabel('Data')
plt.ylabel('Prezzo di Chiusura')
plt.title('Prezzo di Chiusura con Medie Mobili')
plt.legend()
plt.show()

plt.figure(figsize=(14,7))
plt.plot(df['Data'], df['ATR'], label='ATR 14 Giorni', color='orange')
plt.xlabel('Data')
plt.ylabel('ATR')
plt.title('Average True Range (ATR)')
plt.legend()
plt.show()
```

Eseguiamo questi calcoli e visualizzazioni per ottenere le metriche desiderate.

Sembra che non sia possibile eseguire un'analisi dei dati più avanzata in questo momento. Per favore riprova più tardi.

Tuttavia, posso suggerire alcune metriche che possono essere utili per analizzare i dati azionari:

1. **Media (media)**:
 - **Abertura**: Prezzo medio di apertura.
 - **Fechamento**: Prezzo medio di chiusura.
 - **Volume**: volume medio degli scambi.
2. **Mediana**:
 - Fornisce il valore medio del dataset, che può essere più rappresentativo in presenza di valori anomali.
3. **Deviazione standard**:
 - Misura la quantità di variazione o dispersione nei prezzi e nel volume.
4. **Valori minimi e massimi**:
 - **Abertura Min/Max**: Prezzi di apertura minimi e massimi.
 - **Min/Max Fechamento**: Prezzi di chiusura minimi e massimi.
 - **Volume minimo/massimo**: volume di scambi minimo e massimo.
5. **Cambio giornaliero**:
 - La differenza tra i prezzi di chiusura e di apertura per ogni giorno.
 - Media, mediana e deviazione standard delle variazioni giornaliere.
6. **Volatilità**:
 - Calcolato come deviazione standard dei prezzi di chiusura.
7. **Indice di forza relativa (RSI)**:
 - Un indicatore di momentum che misura la velocità e il cambiamento dei movimenti dei prezzi.
8. **Medie mobili**:
 - Media mobile semplice (SMA) per periodi diversi (ad esempio, 10 giorni, 50 giorni).
 - Media mobile esponenziale (EMA).
9. **Prezzo medio ponderato per il volume (VWAP)**:
 - Fornisce il prezzo medio a cui un titolo è stato scambiato durante il giorno, in base sia al volume che al prezzo.

Questi parametri possono fornire una visione completa della performance, della volatilità e dei modelli di trading del titolo.