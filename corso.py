class Corso:
    def __init__(self, codice, titolo, docente):
        self.codice = codice
        self.titolo = titolo
        self.docente = docente

    def __str__(self):
        return f"{self.codice} {self.titolo} {self.docente}"

