import math

def d(x_1,x_2,y_1,y_2):
  resultado=math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
  return resultado
  


x_1=int(input("x en el punto 1 es"))
y_1=int(input("y en el punto 1 es"))
x_2=int(input("x en el punto 2 es"))
y_2=int(input("y en el punto 2 es"))

print(d(x_1, x_2, y_1, y_2))