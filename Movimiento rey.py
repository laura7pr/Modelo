columna= int(input("columna 1"))

fila= int(input("fila 1"))

columna2= int(input("columna 2"))

fila2= int(input("fila2"))

if (columna2==columna+1)and (columna2==columna-1):

  print("si se puede mover")

elif (fila2==fila+1)and(fila2==fila-1):

  print("si se puede")

elif (fila2!=fila+1) and (fila2!=fila-1):

  print("no se puede")

elif(columna2!=columna+1)and(columna2!=columna-1):

  print("no se puede")

elif (columna+1)and(fila+1):

  print("si se puede")

elif (columna-1)and(fila-1):

  print("si se puede")

else:
  print("no se puede")