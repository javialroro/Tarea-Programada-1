#Elaborado por Javier Alonso Rojas Rojas y Gerardo Alberto Gomez Brenes
#Fecha de creacion: 23/09/22 7:00 PM
#Fecha de modificacion: 10/10/22 12:00 PM
#Version de Python 3.10.2

import re

x = "abcdefghijklmnopqrstuvwxyz"
x1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
def obtenerIndices(keyword):
    """
    Funcionalidad: Obtener la posicion de una letra en el abecedario
    Entradas: keyword (str): La letra a buscar
    Salidas: int: La posicion de la letra
    """
    for i in range(len(keyword)):
        for j in range(len(x)):
            if keyword[i] == x[j]:
                return j+1
#Cifrado Cesar
def posletra(x):
    lista = []
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z',' ']
    for i in x:
        t = 0
        for j in alfabeto:
            if i == j:
                lista += [t]
            t += 1
    return lista


def cesarCodifica(x, salto):
    """
    Funcionalidad: Codificar un mensaje con el cifrado Cesar
    Entradas: x str: El mensaje a codificar, salto str: La cantidad de posiciones que se adelantan
    Salidas: final str: El mensaje codificado
    """
    x = x.lower()
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z',' ']
    final = ''
    pos = posletra(x)
    cantAdelantar = 0

    for i in range(len(x)):
        if pos[i] == 26:
            final += ' '
        elif pos[i] + salto > 25:
            cantAdelantar = (pos[i] + salto) - 26
            final = final + alfabeto[cantAdelantar]
        else:
            cantAdelantar = pos[i] + salto
            final = final + alfabeto[cantAdelantar]
    return final


def cesarDecodifica(x, salto):
    """
    Funcionalidad: Decodificar un mensaje con el cifrado Cesar
    Entradas: x str: El mensaje a decodificar, salto str: La cantidad de posiciones que se adelantan
    Salidas: final str: El mensaje decodificado
    """
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z',' ']
    final = ''
    pos = posletra(x)
    cantRetroceder = 0
    for i in range(len(x)):
        if pos[i] == 26:
            final = final + ' '
        elif pos[i] - salto < 0:
            cantRetroceder = 26 - abs(pos[i] - salto)
            final = final + alfabeto[cantRetroceder]
        else:
            cantRetroceder = pos[i] - salto
            final = final + alfabeto[cantRetroceder]
    return final

#Cifrado de llave
def llaveCodifica(mensaje,keyword):
    """
    Funcionalidad: Codificar un mensaje con el cifrado con llave
    Entradas: mensaje str: El mensaje a codificar, keyword str: La llave
    Salidas: string str: El mensaje codificado
    """
    mensaje=mensaje.lower()
    lista= list(mensaje.split(" "))
    string=""
    for i in lista:
        for j in range(len(i)):
            keyword2=''
            w=0
            while len(keyword2)!= len(i):
                if w>=len(keyword):
                    w=0
                keyword2+=str(keyword[w])
                w+=1
            letraN=obtenerIndices(i[j])+obtenerIndices(keyword2[j])
            if letraN>26:
                letraN=letraN-26
            string+=x[letraN-1]
        string+=" "
    return string

def llaveDecodifica(mensaje,keyword):
    """
    Funcionalidad: Deodificar un mensaje con el cifrado con llave
    Entradas: mensaje str: El mensaje a decodificar, keyword str: La llave
    Salidas: string str: El mensaje decodificado
    """
    mensaje = mensaje.lower()
    lista= list(mensaje.split(" "))
    string=""
    for i in lista:
        for j in range(len(i)):
            keyword2=''
            w=0
            while len(keyword2)!= len(i):
                if w >= len(keyword):
                    w = 0
                keyword2 += str(keyword[w])
                w += 1
            letraN = obtenerIndices(i[j])-obtenerIndices(keyword2[j])
            if letraN < 0:
                letraN = letraN+26
            string += x[letraN-1]
        string+=" "
    return string

#XOR----------------------------------------------------------
def xorCodifica(frase,clave):
    """
    Funcionalidad: Codificar un mensaje con el cifrado XOR
    Entradas: frase str: El mensaje a codificar, clave str: La llave
    Salidas: codificado str: El mensaje codificado
    """
    clave = mismotamanno(frase,clave)
    codificado = []
    for i in range(len(clave)):
        codificado += [hex((ord(frase[i])^ord(clave[i])))]
    return codificado

def limpiar(x):
    for i in range(len(x)):
        if re.match('0',x[i]):
            x[i] = x[i][1:]
    return x        
           
def mismotamanno(frase,clave):
    j = 0
    copiaclave = clave
    if len(frase)> len(clave):
        for i in range(len(clave),len(frase)):
            clave += clave[j]
            j += 1
    else:
        clave = ''
        for i in range(len(frase)):
            clave += copiaclave[i]
    return clave

def XOR_decodificar(frase,clave):
    final = ''
    clave = mismotamanno(frase,clave)
    clave = list(clave)
    copiaclave = clave
    copiafrase = frase
    decodificada = ''
    for i in range(len(clave)):
        num1 = int(frase[i].strip('x'), 16) #hexa a decimal 
        num2 = ord(clave[i]) # caracter a decimal
        #print('num1 ',num1)
        #print('num2 ',num2)
        XOR = int(num1)^int(num2) #XOR
        #print('XOR ',XOR)
        #print('Caracter ',chr(XOR))
        #print('---------------------------------------')
        decodificada += chr(XOR) #decimal del XOR a caracter'
    return decodificada


def agregarCero(x):
    j = 0
    for i in x:
        if len(i) < 3:
            x[j] = x[j][1:]
            x[j] = 'x0' + x[j]
        j += 1
    return x


#Cifrado Vigenere-----------------------------------------
def vigenereCodifica(mensaje,cifra):
    """
    Funcionalidad: Codificar un mensaje con el cifrado Vigenere
    Entradas: mensaje str: El mensaje a codificar, cifra str: La cifra a usar
    Salidas: string str: El mensaje codificado
    """
    mensaje = mensaje.lower()
    lista = list(mensaje.split(" "))
    string = ""
    cifra1=int(cifra[0])
    cifra2=int(cifra[1])
    for i in lista:
        for j in range(len(i)):
            if j%2==0:
                letraN=obtenerIndices(i[j])+cifra1
            else:
                letraN=obtenerIndices(i[j])+cifra2
            string += x1[letraN - 1]
        string+=" "
    return string

def vigenereDecodifica(mensaje,cifra):
    """
    Funcionalidad: Decodificar un mensaje con el cifrado Vigenere
    Entradas: mensaje str: El mensaje a codificar, cifra str: La cifra a usar
    Salidas: string str: El mensaje decodificado
    """
    mensaje = mensaje.lower()
    lista = list(mensaje.split(" "))
    string = ""
    cifra1=int(cifra[0])
    cifra2=int(cifra[1])
    for i in lista:
        for j in range(len(i)):
            if j%2==0:
                letraN=obtenerIndices(i[j])-cifra1
            else:
                letraN=obtenerIndices(i[j])-cifra2
            string += x1[letraN - 1]
        string+=" "
    return string
def palabraInversa(x):
    """
    Funcionalidad: Codificar o decodificar un mensaje con el cifrado de palabra inversa
    Entradas: x str: El mensaje a codificar o decodificar
    Salidas: decypher str: El mensaje codificado o decodificado
    """
    if x.find(" ")!=-1:
        lista = list(x.split(" "))
    else:
        lista = [x]
    decypher=""
    npalabra=''
    for i in lista:
        j=(len(i)-1)
        while j>=0:
            npalabra+=str(i[j])
            j -= 1
        npalabra+=" "
    decypher+=npalabra
    return decypher

def fraseInversa(x):
    """
    Funcionalidad: Codificar o decodificar un mensaje con el cifrado de frase inversa
    Entradas: x str: El mensaje a codificar o decodificar
    Salidas: npalabra str: El mensaje codificado o decodificado
    """
    i=(len(x)-1)
    npalabra=''
    while i>=0:
        npalabra+=str(x[i])
        i-=1
    return npalabra

def telefonoCodifica(x):
    """
    Funcionalidad: Codificar un mensaje con el cifrado de telefono
    Entradas: x str: El mensaje a codificar
    Salidas: cifrado str: El mensaje codificado
    """
    x=x.lower()
    cifrado=""
    for i in range(len(x)):
        if x[i]==' ':
            cifrado+="*"
        if x[i]=='a':
            cifrado+="21"
        if x[i]=='b':
            cifrado+="22"
        if x[i]=='c':
            cifrado+="23"
        if x[i]=='d':
            cifrado+="31"
        if x[i]=='e':
            cifrado+="32"
        if x[i]=='f':
            cifrado+="33"
        if x[i]=='g':
            cifrado+="41"
        if x[i]=='h':
            cifrado+="42"
        if x[i]=='i':
            cifrado+="43"
        if x[i]=='j':
            cifrado+="51"
        if x[i]=='k':
            cifrado+="52"
        if x[i]=='l':
            cifrado+="53"
        if x[i]=='m':
            cifrado+="61"
        if x[i]=='n':
            cifrado+="62"
        if x[i]=='o':
            cifrado+="63"
        if x[i]=='p':
            cifrado+="71"
        if x[i]=='q':
            cifrado+="72"
        if x[i]=='r':
            cifrado+="73"
        if x[i]=='s':
            cifrado+="74"
        if x[i]=='t':
            cifrado+="81"
        if x[i]=='u':
            cifrado+="82"
        if x[i]=='v':
            cifrado+="83"
        if x[i]=='w':
            cifrado+="91"
        if x[i]=='x':
            cifrado+="92"
        if x[i]=='y':
            cifrado+="93"
        if x[i]=='z':
            cifrado+="94"
        cifrado +=" "
    return cifrado
def telefonoDecodifica(x):
    """
    Funcionalidad: Decodificar un mensaje con el cifrado de telefono
    Entradas: x str: El mensaje a decodificar
    Salidas: cifrado str: El mensaje decodificado
    """
    cifrado=""
    x=list(x.split(' '))
    for i in range(len(x)):
        if x[i]=='*':
            cifrado+=" "
        elif x[i]=='21':
            cifrado+="a"
        elif x[i]=='22':
            cifrado+="b"
        elif x[i]=='23':
            cifrado+="c"
        elif x[i]=='31':
            cifrado+="d"
        elif x[i]=='32':
            cifrado+="e"
        elif x[i]=='33':
            cifrado+="f"
        elif x[i]=='41':
            cifrado+="g"
        elif x[i]=='42':
            cifrado+="h"
        elif x[i]=='43':
            cifrado+="i"
        elif x[i]=='51':
            cifrado+="j"
        elif x[i]=='52':
            cifrado+="k"
        elif x[i]=='53':
            cifrado+="l"
        elif x[i]=='61':
            cifrado+="m"
        elif x[i]=='62':
            cifrado+="n"
        elif x[i]=='63':
            cifrado+="o"
        elif x[i]=='71':
            cifrado+="p"
        elif x[i]=='72':
            cifrado+="q"
        elif x[i]=='73':
            cifrado+="r"
        elif x[i]=='74':
            cifrado+="s"
        elif x[i]=='81':
            cifrado+="t"
        elif x[i]=='82':
            cifrado+="u"
        elif x[i]=='83':
            cifrado+="v"
        elif x[i]=='91':
            cifrado+="w"
        elif x[i]=='92':
            cifrado+="x"
        elif x[i]=='93':
            cifrado+="y"
        elif x[i]=='94':
            cifrado+="z"
        else:
            return "El caracter en la posicion " + str(i + 1) + " no esta definido en los codigos telefonicos"
    return 'La frase decodificada es la siguiente: ',cifrado

def binarioDecodifica(x):
    """
    Funcionalidad: Codificar un mensaje con el cifrado de binario
    Entradas: x str: El mensaje a codificar
    Salidas: cifrado str: El mensaje codificado
    """
    cifrado=""
    x=list(x.split(' '))
    for i in range(len(x)):
        if x[i]=='*':
            cifrado+=" "
        elif x[i]=='00000':
            cifrado+="a"
        elif x[i]=='00001':
            cifrado+="b"
        elif x[i]=='00010':
            cifrado+="c"
        elif x[i]=='00011':
            cifrado+="d"
        elif x[i]=='00100':
            cifrado+="e"
        elif x[i]=='00101':
            cifrado+="f"
        elif x[i]=='00110':
            cifrado+="g"
        elif x[i]=='00111':
            cifrado+="h"
        elif x[i]=='01000':
            cifrado+="i"
        elif x[i]=='01001':
            cifrado+="j"
        elif x[i]=='01010':
            cifrado+="k"
        elif x[i]=='01011':
            cifrado+="l"
        elif x[i]=='01100':
            cifrado+="m"
        elif x[i]=='01101':
            cifrado+="n"
        elif x[i]=='01110':
            cifrado+="o"
        elif x[i]=='01111':
            cifrado+="p"
        elif x[i]=='10000':
            cifrado+="q"
        elif x[i]=='10001':
            cifrado+="r"
        elif x[i]=='10010':
            cifrado+="s"
        elif x[i]=='10011':
            cifrado+="t"
        elif x[i]=='10100':
            cifrado+="u"
        elif x[i]=='10101':
            cifrado+="v"
        elif x[i]=='10110':
            cifrado+="w"
        elif x[i]=='10111':
            cifrado+="x"
        elif x[i]=='11000':
            cifrado+="y"
        elif x[i]=='11001':
            cifrado+="z"
        else:
            return "El codigo binario"+" en la posicion "+str(i+1)+" no esta definido"
    return print('La frase decodificada es la siguiente: ',cifrado)
def binarioCodifica(x):
    """
    Funcionalidad: Decodificar un mensaje con el cifrado de binario
    Entradas: x str: El mensaje a decodificar
    Salidas: cifrado str: El mensaje decodificado
    """
    x=x.lower()
    cifrado=""
    #x=list(x.split(' '))
    for i in range(len(x)):
        #print("1"+cifrado)
        if x[i]==" ":
            cifrado+='*'
        elif x[i]=='a':
            cifrado+="00000"
        elif x[i]=='b':
            cifrado+="00001"
        elif x[i]=='c':
            cifrado+="00010"
        elif x[i]=='d':
            cifrado+="00011"
        elif x[i]=='e':
            cifrado+="00100"
        elif x[i]=='f':
            cifrado+="00101"
        elif x[i]=='g':
            cifrado+="00110"
        elif x[i]=='h':
            cifrado+="00111"
        elif x[i]=='i':
            cifrado+="01000"
        elif x[i]=='j':
            cifrado+="01001"
        elif x[i]=='k':
            cifrado+="01010"
        elif x[i]=='l':
            cifrado+="01011"
        elif x[i]=='m':
            cifrado+="01100"
        elif x[i]=='n':
            cifrado+="01101"
        elif x[i]=='o':
            cifrado+="01110"
        elif x[i]=='p':
            cifrado+="01111"
        elif x[i]=='q':
            cifrado+="10000"
        elif x[i]=='r':
            cifrado+="10001"
        elif x[i]=='s':
            cifrado+="10010"
        elif x[i]=='t':
            cifrado+="10011"
        elif x[i]=='u':
            cifrado+="10100"
        elif x[i]=='v':
            cifrado+="10101"
        elif x[i]=='w':
            cifrado+="10110"
        elif x[i]=='x':
            cifrado+="10111"
        elif x[i]=='y':
            cifrado+="11000"
        elif x[i]=='z':
            cifrado+="11001"
        else:
            return "El caracter en la posicion " + str(i + 1) + " no esta definido en el alfabeto"
        cifrado+=" "
    return cifrado


#hola

