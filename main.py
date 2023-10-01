fruits = ['banana', 'strawberry', 'apple', 'pear', 'tomatoe']

f = input('Write a fruit: ')
if f in fruits:
  print(f'{f} is on the list.')
else: 
  print('sorry, but the fruit isnt on the list.')

###########################
print('')

fruits.sort()
print(fruits)

###########################
print('')

print(fruits.count('apple'))

###########################
print('')

fruits.append('blueberry')
print(fruits)

###########################
print('')

fruits.extend(['a', 'b', 'c'])
print(fruits)

###########################
print('')

fruits.insert(0, 'new')
print(fruits)

###########################
print('')

numbers = ['one', 'two', 'three', 'four', 'five']

fruits = fruits + numbers
'fruits.extend(numbers)'
print(fruits)

############################
print('')

fruits.reverse()
print(fruits)

###########################
print('')

list1 = fruits.copy()
print(list1)

###########################
print('')

print(len(fruits))

###########################
print('')

fruits.pop()
print(fruits)

###########################
print('')

fruits.pop(5)
print(fruits)

###########################
print('')

fruits.clear()
print(fruits)

###########################
print('')

fruits = ['banana', 'strawberry', 'apple', 'pear', 'tomatoe']
fruits.sort()
print(fruits)

###########################
print('')

curso = 'algoritmos e programacao'
print(curso)
curso = curso.split()
print(curso)

###########################
print('')

print('-'.join(curso))

###########################
print('')

carrinho = []
produto = ''

while produto != 'sair':
  print('Adicione um produto na lista ou digite "sair" para sair:')
  produto = input()
  if produto != 'sair':
    carrinho.append(produto)

for produto in carrinho:
  print(produto)
  
###########################
print('')

carro = 2
veiculos = [carro]
print(veiculos)

###########################
print('')

colors = ['green', 'yellow', 'blue', 'white']
print(colors[2])

###########################
print('')

for color in colors:
  print(color)
indice = 0
'''
while indice < len(colors):
  print(colors[indice])
  indice = indice + 1]
'''

###########################
print('')

for indice, color in enumerate(colors):
  print(indice, color)

####################
print('')

for color in enumerate(colors):
  print(color)

####################
print('')

lista = []
lista.append(1)
lista.append(2)
lista.append(2)
print(lista, 'lista')

####################
print('')

numbers = [1, 2, 3, 4, 5, 6]
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(len(numbers))
