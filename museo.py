# Se voglio utilizzare una classe definita in un altro file o modulo devo usare le parole chiave import e from
from quadro import Quadro # dal file "quadro" importa la classe "Quadro"

# Ora posso utilizzare la classe Quadro (es. per creare oggetti)
q = Quadro("Monet", "...", "...", "...")

print(q.__str__())
# fa anche altre istruzioni perché python prima esegue quadro.py (per capire come è fatta la classe) e poi
# esegue museo.py
# nei file dove si definisce una classe va scritto SOLO è il codice per definire la classe (altrimenti verrà eseguito anche altro codice)

print(q) # Se ho definito la funzione __str__() per l'oggetto quando lo vado a stampare Python capisce che deve
         # utilizzare quella funzione anziché stampare l'indirizzo di memoria


lista_di_quadri = []
lista_di_quadri.append(q)
lista_di_quadri.append(Quadro("Cezanne", "...", "...", "..."))
lista_di_quadri.append(Quadro("Pollock", "...", "...", "..."))

print("Lista di quadri:")
for quadro in lista_di_quadri:
    print(quadro.__str__())


# 1. CON LE CLASSI POSSO DEFINIRE I MIEI TIPI DI DATO (ES. QUADRO)
# 2. POSSO DOTARLI DEI DATI/DEGLI ATTRIBUTI CHE LI CARATTERIZZANO (NASCOSTI)
# 3. POSSO DOTARLI DELLE FUNZIONI/DEI METODI PER OPERARE SU QUEI DATI