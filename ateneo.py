from studente import Studente
from corso import Corso

def main():
    s1 = Studente("1234", "Mario", "Rossi", "20051014")

    print(s1) # Chiama automaticamente __str()__

    s2 = Studente("5678", "Gianni", "Verdi", "20060520")

    lista_studenti = [s1]
    lista_studenti.append(s2)

    c001 = Corso("001", "Programmazione Avanzata", "Lamberti")











main()