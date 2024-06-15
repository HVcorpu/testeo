'''
Clase 22: 
Desafío 1
Desarrolla un programa que permita mostrar los siguientes patrones. Luego 
crear una función para cada uno y un menú que permita seleccionar cuál 
imprimir.

Autor: Horacio Javier Corpu
Fecha:26/05/2024
Revisión: 00
'''
# Bloque de función Triángulo escaleno
def escaleno():
    cont = 10
    cadena =str('*')
    num = int(10) # Cantidad de espacios del contenedor
    while cont >= 2:
        print(cadena.center(num," "))
        cadena = cadena + "**"
        cont = cont - 2

# Bloque de función Rectángulo 8 x 4
def rectangulo():
    cont_1 = int(1)
    cont_2 = int(1)
    cadena =str('*')
    while cont_1 <= 4:
        cont_2 = 1
        while cont_2 <= 8:
            print(cadena,end=' ')
            cont_2 = cont_2 + 1
        print()
        cont_1 = cont_1 + 1

# Bloque de función Rombo
def rombo():
    cont = 10
    cadena =str('*')
    num = int(10)
    while cont >= 2:
        print(cadena.center(num," "))
        cadena = cadena + "**"
        cont = cont - 2
        if cont == 0:
            fin = 7
            while fin >= 1:
                print(cadena[0:fin].center(num,' '))
                fin = fin - 2
            break
# Bloque de función flecha
def flecha():
    espacios = int(11)
    cadena = str(' ')
    cont = int(1)
    while cont <= 7:
        print(cadena.ljust(espacios,'*'))
        espacios = espacios + 1
        cadena = cadena + ' '
        cont = cont + 1
        if cont == 8:
            espacios = int(16)
            long = len(cadena)-2
            fin = int(1)
            while fin <=6:
                cadena_2 = cadena[0:long]
                print(cadena_2.ljust(espacios,'*'))
                long = long - 1
                espacios = espacios - 1
                fin = fin + 1
                            
    
# Bloque funcion principal que se ejecuta primero
def main():
    print()
    print('Graficadora de patrones')
    print()
    opcion = input('''
    Elija una opción del menú para graficar:
    ● 1 - Triángulo escaleno.
    ● 2 - Rectángulo 8 x 4.
    ● 3 - Rombo.
    ● 4 - Flecha.
    ● 5 - Salir.

    : ''' )
    match opcion:
        case "1":
            escaleno()
        case "2":
            rectangulo()
        case "3":
            rombo()
        case "4":
            flecha()
        case "5":
            print ('Fin del programa.')
        case _:
            print ('Error al ingresar la opción.')
            

# Bloque principal
main() #inicio del programa llamando a la función principal