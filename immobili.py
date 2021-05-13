import sqlite3
conn = sqlite3.connect('Agenzia.db')
conn.execute('CREATE TABLE Immobile (immobile_id INTEGER PRIMARY KEY, proprietario, indirizzo, prezzo, catalogo_id)')
conn.execute('CREATE TABLE Catalogo (catalogo_id INTEGER PRIMARY KEY, Classe, PrcMin, PrcMax)')


class Catalogo():

    def __init__(self, Classe, PrcMin, PrcMax):
        self.Classe = Classe
        self.PrcMin = PrcMin
        self.PrcMax = PrcMax
        self.Lista = []

    def inserisci(self):
        self.Lista.append(Immobile)
        print("Immobile inserito nel catalogo")



class Immobile():
    
    def __init__(self, proprietario, indirizzo, prezzo, catalogo):
        self.proprietario = proprietario
        self.indirizzo = indirizzo
        self.prezzo = prezzo
        self.catalogo = catalogo

    def inserimento(self, lista, Catalogo):
        lista.append(self)
        Catalogo.lista.append(self)
        print ("immobile aggiunto con successo")

    def modifica(self):
        print("Inserisci nuovi valori ai campi che vuoi modificare, lascia vuoti i campi da mantenere uguali")
        mproprietario = str(input("Inserisci nuovo proprietario: "))

        if mproprietario != "":
            self.proprietario = mproprietario
        mindirizzo = str(input("Inserisci nuovo indirizzo: "))
        if mindirizzo != "":
            self.indirizzo = mindirizzo
        mprezzo = str(input("Inserisci nuovo prezzo: "))
        if mprezzo != "":
            self.prezzo = mprezzo
    
    def cancellazione(self, lista):
        lista.remove(self)
        print("Immobile rimosso con successo! \n")

    def stampa(self):
        print("Proprietario: %s \nIndirizzo: %s \nPrezzo: %s"  %(self.proprietario, self.indirizzo, self.prezzo))


ListaImmobili = []

#Creo i cataloghi e gli immobili
CatPrestigio = Catalogo("Prestigio", "500", "100000")
CatVacanza = Catalogo("Vacanza", "500", "1500")
CatPop = Catalogo("Popolari", "200", "800")

myImmobile = Immobile("Marco", "via via 7", "2000", "Prestigio")
myImmobile.inserimento(ListaImmobili, Catalogo)
myImmobile.inserimento(ListaImmobili)
myImmobile.modifica()
myImmobile.cancellazione(ListaImmobili)

CercIndirizzo = str(input("Scegli l'indirizzo da cercare: "))

for im in ListaImmobili:
    if im.indirizzo == CercIndirizzo:
        im.stampa()
    else:
        print("indirizzo non trovato")


for im in ListaImmobili:
    im.stampa()



for im in ListaImmobili:
    im.stampa()
