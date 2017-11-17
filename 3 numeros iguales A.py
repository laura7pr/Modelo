n1=int(input("numero 1"))

n2=int(input("numero 2"))

n3=int(input("numero 3"))

if (n1== n2== n3):

  print("iguales")

elif (n1==n2!=n3)or(n1!=n2==n3)or(n1==n3!=n2):

  print("2 iguales")

elif (n1!=n2!=n3):

  print("distintos")