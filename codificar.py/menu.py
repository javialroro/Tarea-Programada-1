#Elaborado por Javier Alonso Rojas Rojas y Gerardo Alberto Gomez Brenes
#Fecha de creacion: 23/09/22 7:00 PM
#Fecha de modificacion: 10/10/22 12:00 AM
#Version de Python 3.10.2

import re
from funciones import *
#cesar-------------------------
def cesar_aux(x,y):
    '''
    funcionalidad: Validar que la frase contenga solo letras y espacios,que el desplazamiento sea un numero,
    y que ninguna este vacía.
    entradas: frase, desplazamiento 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    y = str(y)
    if x == '' or y == '':
        return False,'Tanto frase como la cantidad de desplazamientos no pueden ser vacias. Inténtelo de nuevo'
    for i in x:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'Valor no valido, solo letras como frase. Inténtelo de nuevo. '
    for i in y:
        if not re.match('\d',i):
            return False,'Solo numeros como valor de desplazamiento. Inténtelo de nuevo. '
    if x.strip() and y.strip() != '':
        return True,'si'
    else:
        return False,'Tanto frase como la cantidad de desplazamientos no pueden ser vacias. Inténtelo de nuevo'


def cesarDecodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase,desplazamiento 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase a decodificar: ')
    desplazamiento = input('Ingrese lugares a desplazar en la decodificacion: ') 
    valido,impresion = cesar_aux(frase,desplazamiento)
    if valido != False:
        print('Frase codificada: ',cesarDecodifica(frase,int(desplazamiento)))
    else:
        print(impresion)
        cesarDecodificaES()
        
def cesarCodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase, desplazamiento 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase a codificar: ')
    desplazamiento = input('Ingrese lugares a desplazar en la codificacion: ') 
    valido,impresion = cesar_aux(frase,desplazamiento)
    if valido != False:
        print('Frase decodificada: ',cesarCodifica(frase,int(desplazamiento)))
    else:
        print(impresion)
        cesarCodificaES()
#cifradollave-----------------------------------------------------------
def cifradoLlave_aux(x,y):
    '''
    funcionalidad: Validar que la frase contenga solo letras y espacios, que la clave sean solo letras,
    y que ninguna este vacía.
    entradas: frase, clave 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    if x == '' or y == '':
        return False,'Tanto frase como la clave no pueden ser vacias. Inténtelo de nuevo'  
    for i in x:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'Valor no valido, solo letras como frase. Inténtelo de nuevo. '
    for i in y:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'Valor no valido, solo letras como clave. Inténtelo de nuevo. '
    if x.strip() and y.strip() != '':
        return True,'si'
    else:
        return False,'Tanto frase como la clave no pueden ser vacias. Inténtelo de nuevo'


def cifradoLlaveCodificarES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase, clave 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
''' 
    frase = input('Ingrese frase a codificar: ')
    clave = input('Ingrese clave con la que desea codificar: ')
    valido,impresion = cifradoLlave_aux(frase,clave)
    if valido != False:
        print('Frase codificada: ',llaveCodifica(frase,clave))
    else:
        print(impresion)
        cifradoLlaveCodificarES()

def cifradoLlaveDecodificarES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase, clave 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase a decodificar: ')
    clave = input('Ingrese clave con la que desea decodificar: ')
    valido,impresion = cifradoLlave_aux(frase,clave)
    if valido != False:
        print('Frase decodificada: ',llaveDecodifica(frase,clave))
    else:
        print(impresion)
        cifradoLlaveDecodificarES()        
#XOR----------------------------------------------------
    
def XORcodifica_aux(x,y):
    '''
    funcionalidad: Validar que la frase contenga solo letras y espacios, que la llave sean solo letras,
    y que ninguna este vacía.
    entradas: frase, llave 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    if x == '' or y == '':
        return False,'Tanto frase como llave no pueden ser vacias. Inténtelo de nuevo'         
    for i in x:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'Valor no valido, solo letras como frase. Inténtelo de nuevo. '
    for i in y:
        if not re.match('[A-Za-z]',i):
            return False,'Valor no valido, solo letras como llave. Inténtelo de nuevo. '
    if x.strip() and y.strip() != '':
        return True,'si'
    else:
        return False,'Tanto frase como llave no pueden ser vacias. Inténtelo de nuevo'


def XORdecodifica_aux(x, y):
    '''
    funcionalidad: Validar que la frase sea un numero hexadecimal perteneciente a la tabla ASCII de 8 bits (00 - FF)
    y espacios, que la llave sean solo letras,
    y que ninguna este vacía.
    entradas: frase, llave 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''

    if x == '' or y == '':
        return False, 'Tanto frase como llave no pueden ser vacias. Inténtelo de nuevo'
    for i in x:
        if not re.match(r'x\d\d|x\d[A-Fa-z]|x[A-Fa-z][A-Fa-z]|[A-Fa-z]\d', i) or len(i) > 3:
            return False, 'Valor no valido, solo numeros en base hexadecimal, pertenecientes a la tabla ASCII de 8 bits (00 - FF) '
    for i in y:
        if not re.match('[A-Za-z]', i):
            return False, 'Valor no valido, solo letras como llave. Inténtelo de nuevo. '
    if y.strip() != '':
        return True, 'si'
    else:
        return False, 'Tanto frase como llave no pueden ser vacias. Inténtelo de nuevo'


def XORdecodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase, llave 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    print('x07,x1f....')
    frase = input('Ingrese frase a decodificar, con cada caracter de esta, separado por un espacio, o una coma: ')
    llave = input('Ingrese llave con la que desea codificar: ')
    frase = re.split(r',| ',frase)
    valido,impresion = XORdecodifica_aux(agregarCero(frase),llave)
    if valido != False:
        print('Frase decodificada: ',XOR_decodificar(frase,llave))
    else:
        print(impresion)
        XORdecodificaES()



def XORcodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase, llave 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase a codificar: ')
    llave = input('Ingrese llave con la que desea codificar: ')
    valido,impresion = XORcodifica_aux(frase,llave)
    if valido != False:
        print('Frase codificada: ',' '.join(limpiar(xorCodifica(frase,llave))))
    else:
        print(impresion)
        XORcodificaES()
        
#PalabraInvera---------------------------------------------------------------------------------------------------
 
def palabraInversa_aux(x):
    '''
    funcionalidad: Validar que la frase contenga solo letras y espacios, y que ninguna este vacía.
    entradas: palabra
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''       
    if x == '':
        return False,'La frase no puede ser vacia. Inténtelo de nuevo.'
    for i in x:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'La frase solo debe contener letras o espacios. Inténtelo de nuevo.'
    if x.strip() != '':
        return True,'si'
    else:
        return False,'La frase no puede ser vacia. Inténtelo de nuevo.'


def palabraInversaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: palabra
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    palabra = input('Ingrese la frase que desea codificar: ')
    valido,impresion = palabraInversa_aux(palabra)
    if valido != False:
        print('La codificación de la frase es: ',palabraInversa(palabra))
    else:
        print(impresion)
        palabraInversaES()

def mensajeInversaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: palabra
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    mensaje = input('Ingrese la frase que desea codificar: ')
    valido,impresion = palabraInversa_aux(mensaje)
    if valido != False:
        print('La codificación de la frase es: ',fraseInversa(mensaje))
    else:
        print(impresion)
        mensajeInversaES()
        

#telefonico----------------------------------------------------------------------    

def codigoTelefonicoCodifica_aux(x):
    '''
    funcionalidad: Validar que la frase contenga solo letras y espacios, y que ninguna este vacía.
    entradas: frase
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    if x == '':
        return False,'No se ingresó una frase. Inténtelo de nuevo.'
    for i in x:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'En la frase, solo letras y espacios. Intentelo de nuevo.'
    if x.strip() != '':
        return True,'si'
    else:
        return False,'No se ingresó una frase. Inténtelo de nuevo.'

def codigoTelefonicoDecodifica_aux(x):
    '''
    funcionalidad: Validar que la frase contenga solo numeros, asteriscos (para indicar espacio en la decodificacion),
    espacios y que ninguna este vacía.
    entradas: frase 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    if x == '':
        return False,'No se ingresó una frase. Inténtelo de nuevo.'
    for i in x:
        if not re.match('\d|\*|\s',i):
            return False,'En la frase, solo números, asteriscos entre estos, y espacios. Inténtelo de nuevo.'
    if x.strip() != '':
        return True,'si'
    else:
        return False,'No se ingresó una frase. Inténtelo de nuevo.'
    
def cTelefonicoCodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase que desea codificar: ')
    valido,impresion = codigoTelefonicoCodifica_aux(frase)
    if valido != False:
        print(telefonoCodifica(frase))
    else:
        print(impresion)
        cTelefonicoCodificaES()

def cTelefonicoDecodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase que desea decodificar: ')
    valido,impresion = codigoTelefonicoDecodifica_aux(frase)
    if valido != False:
        print(telefonoDecodifica(frase))
    else:
        print(impresion)
        cTelefonicoDecodificaES()
#binario--------------------------------------------------------------------------
        
def decodificacionBinario_aux(x):
    '''
    funcionalidad: Validar que la frase contenga solo 1s y 0s, asteriscos (para indicar espacio en la decodificacion),
    espacios y que ninguna este vacía.
    entradas: frase 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    if x == '':
        return False,'No deje la frase vacía. Inténtelo de nuevo.'  
    for i in x:
        if not re.match('[10]|\s|\*',i):
            return False,'Solo 1s y 0s en la frase, nada más. Inténtelo de nuevo.'
    if x.strip() != '':
        return True,'si'
    else:
        return False,'No deje la frase vacía. Inténtelo de nuevo.'
    
def codificacionBinario_aux(x):
    '''
    funcionalidad: Validar que la frase contenga solo letras y espacios y que ninguna este vacía.
    entradas: frase 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    if x == '':
        return False,'No deje la frase vacía. Inténtelo de nuevo.'    
    for i in x:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'En la frase, solo letras y espacios. Intentelo de nuevo.'
    if x.strip() != '':
        return True,'si'
    else:
        return False,'No deje la frase vacía. Inténtelo de nuevo.'

def decodificacionBinarioES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase que desea decodificar: ')
    valido, impresion = decodificacionBinario_aux(frase)
    if valido != False:
        print(binarioDecodifica(frase))
    else:
        print(impresion)
        decodificacionBinarioES()
        
def codificacionBinarioES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese frase que desea codificar: ')
    valido, impresion = codificacionBinario_aux(frase)
    if valido != False:
        print('La frase codificada es la siguiente: ',binarioCodifica(frase.lower()))
    else:
        print(impresion)
        codificacionBinarioES()



#Vigenere------------------
def vigenere_aux(x,y):
    '''
    funcionalidad: Validar que la frase contenga solo letras y espacios, que la cifra sean solo numeros
    y que su largo sea de 2 digitos
    entradas: frase,cifra 
    salidas: variable booleana indicando que las entradas son validas o no validas, y un string indicando
    el mensaje a imprimir si no son validas '''
    y = str(y)
    if x == '' or y == '':
        return False,'Tanto frase como la cifra no pueden ser vacías. Inténtelo de nuevo'
    if len(y) != 2:
        return False,'La cifra debe de ser de dos dígitos'
    for i in x:
        if not re.match('[A-Za-z]|[\s]',i):
            return False,'Valor no valido, solo letras como frase. Inténtelo de nuevo. '
    for i in y:
        if not re.match('\d',i):
            return False,'Solo números para cifra. Inténtelo de nuevo. '
    if x.strip() and y.strip() != '':
        return True,'si'
    else:
        return False,'Tanto frase como la cifra no pueden ser vacías. Inténtelo de nuevo'

    
def vigenereCodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase,cifra 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese la frase que desea codificar: ')
    cifra = input('Ingrese la cifra con la que la desea codificar: ')
    valido, impresion = vigenere_aux(frase,cifra)
    if valido != False:
        print('La frase codificada es: ',vigenereCodifica(frase.lower(),cifra))
    else:
        print(impresion)
        vigenereCodificaES()
        
def vigenereDecodificaES():
    '''
    funcionalidad: recibir datos necesarios, generar la salida y realizar el proceso de pedir
    los datos de nuevo si no son validos (basados en resultado funcion aux)
    entradas: frase,cifra 
    salidas: Impresion resultado, o pedir datos de nuevo si no son validos
'''
    frase = input('Ingrese la frase que desea decodificar: ')
    cifra = input('Ingrese la cifra con la que la desea decodificar: ')
    valido, impresion = vigenere_aux(frase,cifra)
    if valido != False:
        print('La frase decodificada es: ',vigenereDecodifica(frase,cifra))
    else:
        print(impresion)
        vigenereDecodifica()
def codificarDecodificar():
    print("1. Codificar\n2. Decodificar")
    opcion = input("Ingrese su opcion: ")
    if opcion == "1":
        return True
    elif opcion == "2":
        return False
    else:
        print("Error, ingrese una opcion valida")
        return codificarDecodificar()
    

#-------------------Programa principal ------------------------------------
def menu():
    print("---------------------------------------------\nBienvenido al sistema de tecnicas de criptografia\n")
    print("1. Cifrado por sustitucion\n2. Cifrado por transposicion\n"
          "3. Cifrado por codigo telefonico\n4. Cifrado por codigo binario\n5. Salir")
    cifrado=input("Seleccione una opcion: ")
    if cifrado=="1":
        print("\n---------------------------------------------")
        print("a. Cifrado Cesar\nb. Cifrado por llave\nc. Sustitucion Vigenere\nd. Cifrado por XOR y llave")
        opcion=input("Seleccione una opcion: ")
        #print("\n")
        if opcion=="a":
            accion=codificarDecodificar()
            if accion==True:
                cesarCodificaES()
            else:
                cesarDecodificaES()
        elif opcion=="b":
            accion=codificarDecodificar()
            if accion==True:
                cifradoLlaveCodificarES()
            else:
                cifradoLlaveDecodificarES()

        elif opcion=="c":
            accion=codificarDecodificar()
            if accion==True:
                vigenereCodificaES()
            else:
                vigenereDecodificaES()

        elif opcion=="d":
            accion=codificarDecodificar()
            if accion==True:
                XORcodificaES()
            else:
                XORdecodificaES()

        else:
            print("\nError, ingrese una opcion valida")
            
    elif cifrado=="2":
        print("\n---------------------------------------------")
        print("a. Palabra inverso\nb. Mensaje inverso\n")
        opcion=input("Seleccione una opcion: ")
        if opcion=="a":
            accion=codificarDecodificar()
            if accion==True:
                palabraInversaES()
            else:
                palabraInversaES()
        elif opcion=="b":
            accion=codificarDecodificar()
            if accion==True:
                mensajeInversaES()
            else:
                mensajeInversaES()
        else:
            print("Error, ingrese una opcion valida")
        
    elif cifrado=="3":
        accion = codificarDecodificar()
        if accion == True:
            cTelefonicoCodificaES()
        else:
            cTelefonicoDecodificaES()
    elif cifrado=="4":
        accion = codificarDecodificar()
        if accion == True:
            codificacionBinarioES()
        else:
            decodificacionBinarioES()
    elif cifrado=="5":
        print("Gracias por usar el sistema")
        return
    else:
        print("\nError, ingrese una opcion valida")
    menu()
menu()
