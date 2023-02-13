class vehicle:   #crea new class
    def __init__(self,name,tipo,color,marca,any,precio):  #Atributs del vehicle
        self.name = name
        self.tipo = tipo
        self.color = color
        self.marca = marca
        self.any = any
        self.precio = precio

    # Getters i Setters dels atributs del vehicle
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo = tipo
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca = marca
    def getAny(self):
        return self.any
    def setAny(self,any):
        self.any = any
    def getPrecio(self):
        return self.precio
    def setPrecio(self,precio):
        self.precio = precio

    # Mètode que retorna els atributs del vehicle
    def salutacio(self):
        print("El nom de aquesta vehicle es " + self.name)
        print("El tipo de aquesta vehicle es " + self.tipo)
        print("El color de aquesta vehicle es " + self.color)
        print("La marca de aquesta vehicle es " + self.marca)
        print("El any de naxiament de aquesta vehicle es " + self.any)
        print("El precio de aquesta vehicle es " + self.precio)