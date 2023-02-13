from book import book
from user import user
from university import university
from animal import animal
from vehicle import vehicle
from school import  school

# INSTÀNCIES DE LA CLASSE BOOK:
ramon = book("Ramón y su Camión", "Divertit", "2018", "JR", "5€", "Dura")
ramon.info()
ramon.setTitol("Camión y su Ramón")
ramon.info()

bongo = book("Bongo Bong", "Tranquil", "2000", "Manel Adeu", "Gratis", "Suau")
bongo.info()
bongo.setAny("2002")
bongo.info()

# INSTÀNCIES DE LA CLASSE USER
goku = user("xXS0nGOKU777Xx", "2 mesos", "2 d'agost del 2014", "3", "Bolívia", "13")
goku.info()
goku.setAmistats("2")
goku.info()

joseluis = user("Jose.Luis.1954", "14 anys", "13 de novembre del 1954", "765", "Catalunya", "1200")
joseluis.info()
joseluis.setPais("Espanya")
joseluis.info()

# INSTÀNCIES DE LA CLASSE UNIVERSITY
masachusets = university("Universitat de Masaxusets", "12.420", "Masaxusets", "2 quilòmetres quadrats", "Ciutat de Masaxusets", "50")
masachusets.info()
masachusets.setEstudiants("11.987")
masachusets.info()

empuriaBrava = university("Universitat d'Empúriabrava", "2.320", "Alt Empordà", "1 quilòmetre quadrat", "Empúriabrava", "23")
empuriaBrava.info()
empuriaBrava.setArea("1,5 quilòmetres quadrats")
empuriaBrava.info()

# INSTÀNCIES DE LA CLASSE ANIMAL:
cat = animal("javier","cat","blanca","5kg","22 meses","l'agrada menja peix")
cat.salutacio()
cat.setColor("negra")
cat.salutacio()
perro = animal("jordi","perro","blue","15kg","40 meses","l'agrada menja os")
perro.salutacio()
perro.setColor("verd")
perro.salutacio()

# INSTÀNCIES DE LA CLASSE VEHICLE:
coche = vehicle("Q3","coche","blanca","audi","2018","13500€")
coche.salutacio()
coche.setColor("negra")
coche.salutacio()
moto = vehicle("Metralla","moto","blue","yamaha","2018","5500€")
moto.salutacio()
moto.setColor("negra")
moto.salutacio()

# INSTÀNCIES DE LA CLASSE SCHOOL:
ins = school("jaume balmes","ciclo informatico","6","256","1962","un institut que te moltes largas historia")
ins.salutacio()
ins.setTipo("batxillerat")
ins.salutacio()
batxi = school("jaume balmes","batxillerat","4","156","1962","un batxillerat que te moltes largas historia")
batxi.salutacio()
batxi.setTipo("institut")
batxi.salutacio()