#Creare una classe Prestito che colleghi un Utente a un Libro e contenga:utente (oggetto Utente)libro (oggetto Libro)giorni (numero di giorni del prestito)
#Aggiungere un metodo dettagli() che stampi tutte le informazioni sul prestito.


from Libro import Libro
from Utente import Utente
class Prestito():
    def __init__(self, utente , libro , giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni
        
    def dettagli(self):
        return f"L'utente {self.utente.nome} ha in prestito il libro {self.libro.titolo} da {self.giorni} giorni"