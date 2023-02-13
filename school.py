class school:     #crea new class
    def __init__(self,name,tipo,clsses,alumnos,any,other):   #Atributs del vehicle
        self.name = name
        self.tipo = tipo
        self.clsses = clsses
        self.alumnos = alumnos
        self.any = any
        self.other = other

    # Getters i Setters dels atributs del school
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo = tipo
    def getClases(self):
        return self.clsses
    def setClases(self,clsses):
        self.clsses = clsses
    def getAlumnos(self):
        return self.alumnos
    def setAlumnos(self,alumnos):
        self.alumnos = alumnos
    def getAny(self):
        return self.any
    def setAny(self,any):
        self.any = any
    def getOther(self):
        return self.other
    def setOther(self,other):
        self.other = other

    # Mètode que retorna els atributs del school
    def salutacio(self):
        print("El nom de aquesta escola es " + self.name)
        print("El tipo de aquesta escola es " + self.tipo)
        print("Hi ha " + self.clsses + " classes en aquesta escola")
        print("Hi ha " + self.alumnos + " alumnos en aquesta escola")
        print("El any de naxiament de aquesta escola es " + self.any)
        print("El otra informacio de aquesta escola es " + self.other)