# Funções #########################################


# Limpar uma lista - tirar valores repetidos
def limp(lista_limp : list) -> list:
    lista_limp = list(set(lista_limp))
    return lista_limp

# Limpar arquivo csv apagar tudo
def limp_csv(arquivo_csv : str):
   with open(file=arquivo_csv, mode='w') as file:
      file.write("")


# Extrair da celula um valor em uma posição
def extcel(lista_divd : list, elemento : int, simb : str, tipo : str) -> list:
   nova_lista = []
   for x in lista_divd:
      x = x.split(sep=simb)
      x = x[elemento]
      x = x.strip()
      if tipo == 'int':
         x = int(x)
         nova_lista.append(x)
      elif tipo == 'float':
         x = float(x)
         nova_lista.append(x)
      elif tipo == 'str':
         x = str(x)
         nova_lista.append(x)
   return nova_lista

# Media total
def media_de_lista(lista_media : list, round_num : int) -> float:
   from functools import reduce
   media = reduce(lambda x, y: x + y, lista_media) # Total
   media = media / len(lista_media) # Dividindo pela quantidade
   media = round(media, round_num)
   return media

def prograss_bar(tempo):
   import time
   from tqdm import tqdm

   for i in tqdm(range(tempo)):
    time.sleep(1)

def attaccare(lista1:list, lista2:list, totale_di_elemnti:int) -> list:
   nuova_lista = []
   for x in range(totale_di_elemnti):
      line = lista1[x] + ';' + lista2[x]
      nuova_lista.append(line)
   return nuova_lista


############################## CLASSES ################################


class ArquivoCSV(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = self._extrair_conteudo()
    self.colunas = self._extrair_nome_colunas()

  def _extrair_conteudo(self):
    conteudo = None
    with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
      conteudo = arquivo.readlines()
    return conteudo

  def _extrair_nome_colunas(self):
    return self.conteudo[0].strip().split(sep=',')

  def extrair_coluna(self, indice_coluna: str):
    coluna = list()
    for linha in self.conteudo:
      conteudo_linha = linha.strip().split(sep=',')
      coluna.append(conteudo_linha[indice_coluna])
    coluna.pop(0)
    return coluna

class Usuario(object):

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade  
    
    def mostrar_proficao(self, proficao):
        print(f"Nome: {self.nome} e profição: {proficao}")
    
    def maior_idade(self):
        if self.idade >= 18:
            print("Maior de idade")
        else:
            print("Menor de idade")

class Categories(object):

   def __init__(self) -> None:
      pass

   def extrair_categorias(self, conteudo:list) -> list:

      # I tuoi dati
      data_str = conteudo


      # Elabora ogni stringa per creare una tupla e aggiungila a una nuova lista
      data = []
      for elemento in data_str:
         colore, temperatura = elemento.split("; ")
         data.append((colore.strip(), int(temperatura)))
      
      # Creiamo un dizionario per sommare le temperature e contare le occorrenze di ciascun colore
      somme = {}
      conteggi = {}

      for colore, temperatura in data:
         if colore not in somme:
            somme[colore] = 0
            conteggi[colore] = 0
         somme[colore] += temperatura
         conteggi[colore] += 1

      # Calcoliamo la media per ciascun colore
      medie = {colore: somma / conteggi[colore] for colore, somma in somme.items()}

      # Stampiamo le medie
      for colore, media in medie.items():
         print(f'La media per {colore} è {media}')

def valore_abbreviato(valore:str) -> str:
    alg_valore = list(valore)
    num_punt = sum(map(lambda x: x == '.', valore))
    for x in range(num_punt):
     alg_valore.remove('.')
    numero = int("".join(alg_valore))
    numero_format = "{:,}".format(numero).replace(",", ".")
    return numero_format
