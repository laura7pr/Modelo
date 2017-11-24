columna= int(input("columna"))

fila= int(input("fila"))

columna2= int(input("columna2"))

fila2= int(input("fila2"))

if (columna+fila)%2==0 and (columna2+fila2)%2==0:

  print ("Igual")

elif (columna+fila)%2!=0 and (columna2+fila2)%2!=0:

  print ("Igual")
#if (columna+fila)%2==0 and (columna2+fila2)%2!=0:

#  print ("Distinta")

#elif (columna+fila)%2!=0 and (columna2+fila2)%2==0:

#  print ("Distinta")


else:

  print ("Distinto")