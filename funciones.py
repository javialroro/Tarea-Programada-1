#Prueba
def obtenerIndices(keyword):
    x = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(keyword)):
        for j in range(len(x)):
            if keyword[i] == x[j]:
                return j+1
def KeyCypher(mensaje,keyword):
    x = "abcdefghijklmnopqrstuvwxyz"
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
            if letraN==1:
                string+=x[letraN]
            else:
                string+=x[letraN-1]
        string+=" "
    print(string)

#string="hola"
#print(obtenerIndices(string[0]))
KeyCypher("tarea programada de codificacion","tango")