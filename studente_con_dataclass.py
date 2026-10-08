from dataclasses import dataclass

@dataclass
class Studente:
    __matricola: str
    __nome: str
    __cognome: str
    __data_nascimento: str

    # In questo modo Python crea in automatico varie funzioni con i dundescore (metodi getter e setter per
    # attributo, __init__, __str__, __repr__, ...)
