from book import book
from user import user
from university import university

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