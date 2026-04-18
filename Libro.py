#Creare una classe Libro con attributi:titoloautoreannocopie_disponibili
#Aggiungere un metodo info() che restituisca una stringa descrittiva del libro.

class Libro():
    def __init__(self, titolo,autore,anno,copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
    
    def disponibile(self):
        if self.copie_disponibili >= 1:
            #return 'Disponibile'
            return True
        else:
            #return 'Non disponibile' 
            return False
        
    def info(self):
        return f"{self.titolo} ({self.autore}, {self.anno}) - {self.copie_disponibili} copie - {self.disponibile()}"
        