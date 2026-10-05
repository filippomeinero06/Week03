class Quadro:
    def __init__(self, artista, titolo, materiali, anno):
        # _attributo -> attributo e "privato", è meglio non toccarlo (ma comunque qualcuno può modificarlo)
        # __attributo -> attributo sempre "privato" ma questa volta se qualcuno prova a modificarlo, python da errore e lo impedisce
        self.__artista = artista
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno # 1853-1890

    def imposta_anno(self, nuovo_anno):
        if 1853 < nuovo_anno < 1890:
            self.__anno = nuovo_anno
        else:
            print(f"L'anno {nuovo_anno} inserito non è valido")

    def leggi_anno(self):
        return self.__anno


q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", 1870)

# Questa stampa non funziona se i campi sono nascosti, devo scrivere una funzione che restituisca gli attributi
# print(f"Artista: {q1.__artista}\n"
#       f"Titolo: {q1.__titolo}\n"
#       f"Materiali: {q1.__materiali}\n"
#       f"Anno: {q1.__anno}")

# q1.__anno = 1945 # Non posso farlo così perché l'attributo è privato/nascosto

# Per accedere all'attributo devo usare i metodi/funzioni
q1.imposta_anno(1855)

print("Anno: " + str(q1.leggi_anno()))
