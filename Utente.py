#Creare una classe Utente con attributi:nomeetaid_utente
#Aggiungere un metodo scheda() che stampi i dati dell’utente.

class Utente():
    def __init__(self, nome,età,id_utente):
        self.nome = nome
        self.età = età
        self.id_utente = id_utente
        
    def scheda(self):
        return f"Nome: {self.nome} - Età: {self.età} - ID: {self.id_utente}"
    
    