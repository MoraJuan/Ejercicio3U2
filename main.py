from Registro import Registro
import csv
if __name__ == '__main__':
    listaObjeto=[]
    
    
    for i in range(30):
        listaObjeto.append([0]*24)
            
    archivo=open('mes.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        dia = int(fila[0])
        hora = int(fila[1])
        temperatura = float(fila[2])
        humedad = fila[3]
        presion = fila[4]
        UnRegistro = Registro(dia, hora, temperatura, humedad, presion)
        listaObjeto[dia-1][hora-1]=UnRegistro
    
        
        
    listaObjeto[4][8].mostrar()   
    UnRegistro.TemperaturaMaxima(listaObjeto)
    UnRegistro.TemperaturaMinima(listaObjeto)