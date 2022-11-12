class Agregar:
    __arreglo = []
    __indice = ""
    __x=None
    __suma1=0
    __suma2=0
    __suma3=0
    __suma4=None
    #Metodo Agregar
    def agregar(self, objetito):
         
         if objetito.getcodigo() in (self.__x.getcodigo() for self.__x in self.__arreglo):
             indice= self.__arreglo.index(self.__x)
             self.__arreglo[indice]=objetito
         else:
             self.__arreglo.append(objetito)
    
    
    #Metodo buscar
    def buscar(self, codigo):
        for a in self.__arreglo:
            if a.getcodigo() == codigo:
                self.__indice = self.__arreglo.index(a)
                return self.__arreglo[self.__indice]
          

    #Eliminar
    def eliminar(self,codigo):
        for a in self.__arreglo:
            if a.getcodigo() == codigo:
                self.__indice = self.__arreglo.index(a)
                self.__arreglo.pop(self.__indice)

    def credito(self):
        self.__suma1=0
        self.__suma2=0
        self.__suma3=0
        for elem in self.__arreglo:
            if int(elem.getestado()) == 0:
                self.__suma1 += elem.getcredito()
            if int(elem.getestado()) == 1:
                self.__suma2 += elem.getcredito() 
            if int(elem.getestado()) == -1 and int(elem.getobli()) == 1:
                self.__suma3 += elem.getcredito()

        return (self.__suma1, self.__suma2, self.__suma3)
    
    def credHasta(self,semestre):
        self.__suma4=0
        if semestre>10 or semestre<0:
            return 
        for x in self.__arreglo:
            if int(x.getsemestre()) <= semestre and int(x.getobli()) == 1:
                self.__suma4 += x.getcredito()
        return self.__suma4


    def sumarCred2(self,semestre):
        self.__suma1=0
        self.__suma2=0
        self.__suma3=0
        self.__suma4=0
        if semestre>10 or semestre<=0:
            return 
        for elem in self.__arreglo:
            if int(elem.getestado()) == 0 and int(elem.getsemestre())==semestre:
                self.__suma1 += elem.getcredito()
            if int(elem.getestado()) == 1 and int(elem.getsemestre())==semestre:
                self.__suma2 += elem.getcredito()
            if int(elem.getestado()) ==-1 and int(elem.getobli())==1 and int(elem.getsemestre())==semestre:
                self.__suma3 += elem.getcredito()
        return (self.__suma1, self.__suma2, self.__suma3)

    def getArreglo(self):
        return self.__arreglo