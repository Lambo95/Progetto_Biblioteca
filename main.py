""" Parte 2 – Strutture dati
Creare una lista con almeno 5 titoli di libri.
Creare un dizionario che mappi il titolo del libro al numero di copie disponibili.
Creare un insieme (set) che contenga tutti gli utenti registrati alla biblioteca. """

from Libro import Libro
from Utente import Utente
from Biblioteca import Biblioteca

lista_libri = []

lista_libri.append(Libro("Il nome della rosa","Umberto Eco",1980,5))
lista_libri.append(Libro("1984","George Orwell",1949,4))
lista_libri.append(Libro("Il signore degli anelli","J.R.R. Tolkien",1954,0))
lista_libri.append(Libro("La coscienza di Zeno","Italo Svevo",1923,3))
lista_libri.append(Libro("Harry Potter e la pietra filosofale","J.K. Rowling",1997,5))

dizionario_libri = {}

for libro in lista_libri:
    dizionario_libri[libro.titolo] = {
        "copie_disponibili": libro.copie_disponibili
    }

lista_utenti = []

lista_utenti.append(Utente("Marco",19,"U1"))
lista_utenti.append(Utente("Giulia",85,"U2"))
lista_utenti.append(Utente("Luca",20,"U3"))
lista_utenti.append(Utente("Sara",18,"U4"))
lista_utenti.append(Utente("Paolo",32,"U5"))

set_utenti = set(lista_utenti)

#cicli
""" for libro in lista_libri:
    print(libro.info()) """

""" for libro in lista_libri:
    print(libro.__dict__) """

""" print(dizionario_libri) """

""" for utente in set_utenti:
    print(utente.scheda()) """
    
#Prestito
biblioteca = Biblioteca()

biblioteca.presta_libro(lista_utenti[3],lista_libri[1],0)


