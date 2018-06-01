cantidad = 0
grande = 0
posicion = 0
posicion1 = 0
while True:
  n = int(input('Dime un número:'))
  posicion += 1
  if n < grande:
    grande = grande
  else:
    grande = n
    posicion1 = posicion
  cantidad += 1
  if n == 0:
    break
print('El número más grande de la cadena es' +' '+ str(grande) +' y está en la posición' +' '+ str(posicion1))