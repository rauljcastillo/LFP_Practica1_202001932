class Objeto:
    def __init__(self,codigo, nombre,pre,obliga,semestre,creditos,estado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__pre=pre
        self.__obliga=obliga
        self.__semestre=semestre
        self.__creditos=creditos
        self.__estado=estado


    def getcodigo(self):
        return self.__codigo

    def getnombre(self):
        return self.__nombre

    def getpre(self):
        return self.__pre
    
    def getobli(self):
        return self.__obliga
    
    def getsemestre(self):
        return self.__semestre
    
    def getcredito(self):
        return self.__creditos
    
    def getestado(self):
        return self.__estado
