frase=str(input("dime una frase:"))

palabra=str(input("¿que letra buscas?"))

primera =frase .find(palabra)

print(primera+1)

segunda =frase .rfind(palabra)

print(segunda+1)