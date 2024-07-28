# 1. Escreva uma função que receba uma lista de números e retorne outra lista
# com os números ímpares.

def acha_impar(lista):
  impares = []
  for i in lista:
    if i%2 != 0:
      impares.append(i)
  return impares

lista1 = [1,2,3,4,5,6,7,8,9,10,11]
print('Questao 1:\n', acha_impar(lista1), '\n')

# 2. Escreva uma função que receba uma lista de números e retorne outra lista
# com os números primos presentes.

def acha_primos(lista):
  primos = []
  for i in lista:
    primo = True
    if i <= 1:
      primo = False
    for j in range(2,i//2 + 1): # os números acima de i/2 nunca são divisores
      if i%j == 0: # O +1 é por causa de como o in range do python trabalha
        primo = False # Sem ele, 4 seria dado como primo
        break
    if primo:
      primos.append(i)
  return primos

lista2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print('Questao 2:\n', acha_primos(lista2), '\n')

# 3. Escreva uma função que receba duas listas e retorne outra lista com os
# elementos que estão presentes em apenas uma das listas.

def acha_unicos(lista1, lista2):
  unicos = []
  for i in lista1:
    if i not in lista2:
      unicos.append(i)
  for j in lista2:
    if j not in lista1:
      unicos.append(j)
  return unicos

lista3 = [1,2,3,4,6,78,90,45,20]
lista4 = [1,3,4,5,6,54,23,90,20]
print('Questao 3:\n', acha_unicos(lista3, lista4), '\n')

# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o
# segundo maior valor na lista.

def segundo_maior(lista):
  for i in range(len(lista)):
    for j in range(len(lista)-1):
      if lista[j] < lista[j+1]:
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp
  return lista[1]

lista5 = [1,12,32,4,6,78,90,45,20]
print('Questao 4:\n', segundo_maior(lista5), '\n')

# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o
# nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
# pessoas em ordem alfabética.

def ordena_nome(lista):
  for i in range(len(lista)):
    for j in range(len(lista)-1):
      if lista[j][0] > lista[j+1][0]:
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp
  return lista

lista6 = [('Renan',22),('CB',19),('Adriano',34),('Julius',6)]
print('Questao 5:\n', ordena_nome(lista6), '\n')

# 6. Observe os espaços sublinhados e complete o código.

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
                        layout="constrained")
for row in range(2):
  for col in range(2):
    axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                           transform=axs[row, col].transAxes,
                           ha='center', va='center', fontsize=18,
                           color='darkgrey')
fig.suptitle('plt.subplots()')

# 7. Observe os espaços sublinhados e complete o código.

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um
# DataFrame e exibir as primeiras linhas?

import pandas as pd
dataframe = pd.read_csv('https://raw.githubusercontent.com/atlantico-academy/datasets/main/diamonds.csv')
print('Questao 8:\n', dataframe.head(4), '\n')

# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas
# em um “DataFrame” com base em uma condição?

print('Questao 9:\n', dataframe['price'])
print(dataframe.loc[dataframe['cut'] == 'Premium'], '\n')

# 10.Utilizando pandas, como lidar com valores ausentes (NaN) em um
# DataFrame?

# Vendo a quantidade de valores audentes
valores_ausentes = dataframe.isna().sum()
print('Questao 10\n', valores_ausentes, '\n')

# preencher valores ausentes
dataframe.fillna('valor',inplace=True)

# removendo linhas com valores ausentes
dataframe.dropna(inplace=True)

print('Questao 6 e 7:\n')
