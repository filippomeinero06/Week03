class Quadro:
    # Costruttore che costruisce gli oggetti di classe Quadro e li inizializza
    def __init__(self, artista, titolo, materiali, anno):
        # _attributo -> attributo e "privato", è meglio non toccarlo (ma comunque qualcuno può modificarlo)
        # __attributo -> attributo sempre "privato" ma questa volta se qualcuno prova a modificarlo, python da errore e lo impedisce
        self.__artista = artista  # Privati/Nascosti (con _ per scoraggiare o __ per bloccare l'accesso)
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno # 1853-1890


    # Questo serve per ogni attributo che nascondiamo (2 metodi: GETTER e SETTER)
    # Metodo GETTER (leggere il valore di un attributo nascosto)
    @property
    def anno(self):
        return self.__anno

    # Metodo SETTER (impostare il valore di un attributo nascosto)
    @anno.setter
    def anno(self, anno):
        self.__anno = anno # eventualmente posso aggiungere dei controlli (es. if) per controllare errori


    # Metodo che consente al quadro di descriversi come stringa
    # __str__ come alternativa a nomi più bizzarri come descriviti(self), ...
    def __str__(self):
        return (f"{self.__artista}, {self.__titolo}, {self.__materiali}, {self.__anno}")


q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", 1870)

# Questa stampa non funziona se i campi sono nascosti, devo scrivere una funzione che restituisca gli attributi
# print(f"Artista: {q1.__artista}\n"
#       f"Titolo: {q1.__titolo}\n"
#       f"Materiali: {q1.__materiali}\n"
#       f"Anno: {q1.__anno}")

# q1.__anno = 1945 # Non posso farlo così perché l'attributo è privato/nascosto

# Per accedere all'attributo devo usare i metodi/funzioni
# q1.imposta_anno(1855)

# print("Anno: " + str(q1.leggi_anno()))

# print("Anno: " + str(q1.anno)) # Diventa di nuovo possibile perché abbiamo definito il metodo GETTER


# Come faccio a stampare il quadro
# print(q1) # indirizzo area di memoria

# print(q1.artista)

# Per stampare tutti gli attributi (sono privati) dovrei scivere per ognuno un metodo getter, e poi eventualmente
# un setter per modificare i valori

# Chi meglio del quadro può stampare un quadro?
# print(q1.descriviti()) # ho DELEGATO al quadro il compito di stamparsi

print(q1.__str__())