class Immobile():
    
    def __init__(self, rifprop, indirizzo, prezzo):
        self.rifprop = rifprop
        self.indirizzo = indirizzo
        self.prezzo = prezzo

    def inserimento(self, lista):
        lista.append(self)
        print ("immobile aggiunto con successo")

    def modifica(self):
        print("Inserisci nuovi valori ai campi che vuoi modificare, lascia vuoti i campi da mantenere uguali")
        mrifprop = str(input("Inserisci nuovo proprietario: "))

        if mrifprop != "":
            self.rifprop = mrifprop
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
        print("Proprietario: %s \nIndirizzo: %s \nPrezzo: %s"  %(self.rifprop, self.indirizzo, self.prezzo))


ListaImmobili = []

myImmobile = Immobile("Marco", "via via 7", "4")
myImmobile.inserimento(ListaImmobili)
myImmobile.inserimento(ListaImmobili)
myImmobile.modifica()

CercIndirizzo = str(input("Scegli l'indirizzo da cercare: "))

for im in ListaImmobili:
    if im.indirizzo == CercIndirizzo:
        im.stampa()
    else:
        print("indirizzo non trovato")


'''
for im in ListaImmobili:
    im.stampa()

myImmobile.cancellazione(ListaImmobili)

for im in ListaImmobili:
    im.stampa()
    '''
