from Registro import Registro
import csv
if __name__ == '__main__':
    dia = 30
    hora = 24
    listaObjeto=[]
    
    
    for i in range(hora):
        listaObjeto.append([0] * dia)
        
    archivo=open('mes.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        dia = int(fila[0])
        hora = int(fila[1])
        temp = fila[2]
        humedad = fila[3]
        presion = fila[4]
        listaObjeto[dia][hora]=Registro(dia, hora, temp, humedad, presion)
        
    numero=int(input('Ingrese numero de VP : '))
    opcion = None

    for objeto in listaObjeto:
        if numero == objeto.getNumero():
            while opcion!='d':
                print('a- Cant millas')
                print('b- Acum millas')
                print('c- Canjear millas')
                print('d- Salir')
                opcion=input('\nIngrese opcion: ')
                    
