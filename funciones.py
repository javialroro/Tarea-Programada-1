#Prueba
x = "abcdefghijklmnopqrstuvwxyz"
x1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
ascii= '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f'
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
        if x[i]=='a':
            cifrado+="21"
    return print(cifrado)
