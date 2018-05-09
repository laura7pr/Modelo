def potencia (x,n):
  if n==0:
    return 1
  return x *potencia(x,(n-1))
  
n=int(input("dime un numero"))
e=int(input("dime un numero para elevar el primer numero"))
print(potencia (n,e))