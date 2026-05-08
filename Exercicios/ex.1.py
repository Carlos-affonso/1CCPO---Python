pessoas = ['Carlos', 'Murilo', 'Temitope', 'Igor', 'Gabi', 'Gabriel', 'Marcelo']
contador = 0
for i in range(len(pessoas)):
  for j in range (i+1, len(pessoas)):
    print (pessoas[i], "e ", pessoas[j])
    contador += 1

    print('Total de duplas:', contador)


