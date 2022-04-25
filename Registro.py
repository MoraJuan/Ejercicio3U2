class Registro:
    __dia = ''
    __hora = ''
    __temperatura = ''
    __humedad = ''
    __presion = ''
    
    def __init__(self,dia , hora,temperatura, humedad, presion):
        self.__dia = dia
        self.__hora = hora
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    def getTemperatura(self):
        return self.__temperatura
    def getDia(self):
        return self.__dia
    def getHora(self):
        return self.__hora
    def mostrar(self):
        print (str(self.__dia)+','+str(self.__temperatura)+','+str(self.__humedad)+','+str(self.__presion))
    def TemperaturaMaxima(self, listaObjeto):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getTemperatura() > maximo:
                    maximo = listaObjeto[i][j].getTemperatura()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Temperatura maxima registrada: {} en el dia {} hora {}'. format(maximo, dia, hora))
    def TemperaturaMinima(self, listaObjeto):
        minimo = 9999999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getTemperatura() < minimo:
                    minimo = listaObjeto[i][j].getTemperatura()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Temperatura maxima registrada: {} en el dia {} hora {}'. format(minimo, dia, hora))
        
   

