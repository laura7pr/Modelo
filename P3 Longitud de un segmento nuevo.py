import math 

def potencia (x,n):
  if n==0:
    return 1
  return x *potencia(x,(n-1))
  
def l(x_1,x_2,x_3,x_4):
  resultado=math.sqrt(potencia((x_2-x_1),2) + potencia((y_2-y_1),2))
  return resultado
  
x_1=int(input("x en el punto 1 es"))
y_1=int(input("y en el punto 1 es"))
x_2=int(input("x en el punto 2 es"))
y_2=int(input("y en el punto 2 es"))

print(l(x_1,x_2,y_1,y_2))


