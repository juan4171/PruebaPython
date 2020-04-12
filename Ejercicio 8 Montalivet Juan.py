def es_primo(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
    if num == 2:
        return True
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
        return True    

letras={}   #creo un diccionario para guardar las letras y las veces que se repiten
palabra= input('Ingrese una palabra para determinar si la cantidad total de veces que aparece cada letra es un número primo: ')
for x in palabra.lower():
    if x in letras:
        letras[x] += 1
    else:
        letras[x] = 1

primos=[]   # creo una lista para guardas las letras que se repiten un numero primo de veces
print('Palabra ingresada: ',palabra)
for y in letras:
    if letras[y] == 1:
        print('La letra {0} aparece: 1 vez'.format(y))
    else:
        print('La letra {0} aparece: {1} veces'.format(y,letras[y]))
    if es_primo(letras[y]):     #imprimo cuantas veces se repiten las letras y las guardo si se repiten un nro primo de veces
        primos.append(y)

if primos:
    print('Por lo tanto la/las letras: ',end="")
    for elemento in primos:
        print(elemento,end=" ")
    print('son letras que aparecen un número primo de veces.')
else:
    print('En la palabra ingresada no hay letras que se repitan un numero primo de veces.')
