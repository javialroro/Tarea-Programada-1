#Prueba
x = "abcdefghijklmnopqrstuvwxyz"
x1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
def obtenerIndices(keyword):
    for i in range(len(keyword)):
        for j in range(len(x)):
            if keyword[i] == x[j]:
                return j+1
#Cifrado de llave
def KeyCypher(mensaje,keyword):
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
    return print("Mensaje encriptado: "+string)
def KeyDecypher(mensaje,keyword):
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
    return print("Mensaje decriptado: "+string)
#Cifrado Vigenere
def vigenereCypher(mensaje,cifra):
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
    return print("Mensaje encriptado: " + string)

def vigenereDecypher(mensaje,cifra):
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
    return print("Mensaje encriptado: " + string)


#Cifrado XOR
def xorCypher(keyword,cipher):
    lista = list(keyword.split(" "))
    lista2 = []
    for i in lista:
        for j in range(len(i)):
            keyword2 = ''
            w = 0
            while len(keyword2) != len(i):
                if w >= len(cipher):
                    w = 0
                keyword2 += str(cipher[w])
                w += 1
            print(keyword2)
            lista2+= chr(ord(i[j])^ord(keyword2[j]))
    print(lista2)

<<<<<<< Updated upstream
=======
#vigenereCypher('tarea programada','99')
#vigenereDecypher("cjanj yaxpajvjmj",'99')
>>>>>>> Stashed changes
#xorCypher("tarea programada","secreto")

def palabraInverso(x):
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
    return print(decypher)

def fraseInversa(x):
    i=(len(x)-1)
    npalabra=''
    while i>=0:
        npalabra+=str(x[i])
        i-=1
    return print(npalabra)

def telephoneCypher(x):
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
        cifrado+=" "
    return print(cifrado)

telephoneCypher("a")
telephoneCypher("a")


def telephoneDecypher(x):
    cifrado=""
    x=list(x.split(' '))
    for i in range(len(x)):
        if x[i]=='*':
            cifrado+=" "
        if x[i]=='21':
            cifrado+="a"
        if x[i]=='22':
            cifrado+="b"
        if x[i]=='23':
            cifrado+="c"
        if x[i]=='31':
            cifrado+="d"
        if x[i]=='32':
            cifrado+="e"
        if x[i]=='33':
            cifrado+="f"
        if x[i]=='41':
            cifrado+="g"
        if x[i]=='42':
            cifrado+="h"
        if x[i]=='43':
            cifrado+="i"
        if x[i]=='51':
            cifrado+="j"
        if x[i]=='52':
            cifrado+="k"
        if x[i]=='53':
            cifrado+="l"
        if x[i]=='61':
            cifrado+="m"
        if x[i]=='62':
            cifrado+="n"
        if x[i]=='63':
            cifrado+="o"
        if x[i]=='71':
            cifrado+="p"
        if x[i]=='72':
            cifrado+="q"
        if x[i]=='73':
            cifrado+="r"
        if x[i]=='74':
            cifrado+="s"
        if x[i]=='81':
            cifrado+="t"
        if x[i]=='82':
            cifrado+="u"
        if x[i]=='83':
            cifrado+="v"
        if x[i]=='91':
            cifrado+="w"
        if x[i]=='92':
            cifrado+="x"
        if x[i]=='93':
            cifrado+="y"
        if x[i]=='94':
            cifrado+="z"
        #cifrado+=" "
    return print(cifrado)
telephoneCypher("tarea programada")
telephoneDecypher("81 21 73 32 21 * 71 73 63 41 73 21 61 21 31 21")

