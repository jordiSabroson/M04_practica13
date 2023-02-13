class user:
    def __init__(self, username, antiguitat, naixement, amistats, pais, seguidors):
        self.username = username
        self.antiguitat = antiguitat
        self.naixement = naixement
        self.amistats = amistats
        self.pais = pais
        self.seguidors = seguidors

    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username = username

    def getAntiguitat(self):
        return self.antiguitat
    def setAntiguitat(self, antiguitat):
        self.antiguitat = antiguitat

    def getNaixement(self):
        return self.naixement
    def setNaixement(self, naixement):
        self.naixement = naixement

    def getAmistats(self):
        return self.amistats
    def setAmistats(self, amistats):
        self.amistats = amistats

    def getPais(self):
        return self.pais
    def setPais(self, pais):
        self.pais = pais

    def getSeguidors(self):
        return self.seguidors
    def setSeguidors(self, seguidors):
        self.seguidors = seguidors

    def info(self):
        print("Nom d'usuari: "+self.username+"\nAntiguitat: "+self.antiguitat+"\nNaixement: "+self.naixement+"\nAmistats: "+self.amistats+"\nPais: "+self.pais+"\nSeguidors: "+self.seguidors+"\n")