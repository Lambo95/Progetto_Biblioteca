#Creare una funzione presta_libro(utente, libro, giorni) che:
#    1. Verifichi se il libro ha almeno 1 copia disponibile
#        Se sì → riduca il numero di copie e crei un nuovo oggetto Prestito
#        Se no → stampi un messaggio di errore
#    2. Simulare almeno 3 prestiti con utenti e libri diversi.
#    3.Stampare a video:
#        L’elenco aggiornato delle copie disponibili per ciascun libro e dettagli di ogni prestito effettuato
from Libro import Libro
from Utente import Utente
from Prestito import Prestito

class Biblioteca():
    def __init__(self):
        pass
    
    def presta_libro(self, utente, libro, giorni):
        if libro.disponibile():
            prestito = Prestito(utente, libro, giorni)
            libro.copie_disponibili -= 1
            print(f'Il libro "{libro.titolo}" è stato prestato a {utente.nome} per {giorni} giorni')
            print(type(utente))
        else:
            print('Non ci sono copie disponibili')
    
        
        
        
