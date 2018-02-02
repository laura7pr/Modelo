n=int(input("¿cuantos numeros quieres decirme?"))

j=0

for i in range(1,n+1):

  cosa=int(input("dime el " + str(i) + "º numero"  ))

  if (cosa==0):

    j=j+1

    print ("+ un 0")

  else:

    print("no es 0")

print("hay",j, "ceros")
