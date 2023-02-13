class university:
    def __init__(self, nom, estudiants, ciutat, area, ubicacio, cursos):
        self.nom = nom
        self.estudiants = estudiants
        self.ciutat = ciutat
        self.area = area
        self.ubicacio = ubicacio
        self.cursos = cursos

    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom = nom

    def getEstudiants(self):
        return self.estudiants
    def setEstudiants(self, estudiants):
        self.estudiants = estudiants

    def getCiutat(self):
        return self.ciutat
    def setCiutat(self, ciutat):
        self.ciutat = ciutat

    def getArea(self):
        return self.area
    def setArea(self, area):
        self.area = area

    def getUbicacio(self):
        return self.ubicacio
    def setUbicacio(self, ubicacio):
        self.ubicacio = ubicacio

    def getCursos(self):
        return self.cursos
    def setCursos(self, cursos):
        self.cursos = cursos

    def info(self):
        print("Nom: "+self.nom+"\nEstudiants: "+self.estudiants+"\nCiutat: "+self.ciutat+"\nArea: "+self.area+"\nUbicació: "+self.ubicacio+"\nCursos: "+self.cursos+"\n")