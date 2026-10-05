# Definisco un nuovo tipo di dato, la classe Car
class Car: # Per convenzione le classi hanno iniziale maiuscola
    wheels = 4 # Variabile di classe, identica per tutte le istanze di quella classe

    def __init__(self, license_plate, color): # Costruttore della classe
        self.license_plate = license_plate # Attributi o variabili di istanza
        self.color = color
        self.turned_on = False

    # Metodo per verniciare le macchine
    def paint(self, color):
        self.color = color

    # Metodo per accendere le macchine
    def turn_on(self):
        self.turned_on = True


#c1 = Car() # Creo un oggetto di classe/tipo Car

#print(c1)

#c1.license_plate = "GE888EG"

c1 = Car("AA123BB", "Red") # Invoco il costruttore passando 2 argomenti/parametri

print("License plate: " + str(c1.license_plate))
print("Color: " + str(c1.color))
print("Turned on: " + str(c1.turned_on))

c2 = Car("ZZ999ZZ", "Black")

#c1.wheels = 7

#print(c1.wheels)
#print(c2.wheels)

# Come si accede alle variabili di istanza
c1.color = "Green"

# Come si accede alle variabili di classe
Car.wheels = 7 # come se fosse una variabile globale per tutta la classe (non servono a molto)

# Come faccio a cambiare il colore di un oggetto Car?
c1.color = "Pink"
# Come faccio a cambiare lo stato di accensione di un oggetto Car?
c2.turned_on = True

# Anziché accedere direttamente agli attributi, posso usare le funzioni (metodi)
c1.paint("Violet")
c2.turn_on()


# Il programmatore può, tipicamente per sbaglio, andare a definire altre variabili scrivendo
# nome_oggetto.nome_variabile, ma quella sarà propria solo di quella istanza e non di tutti
# gli oggetti creati con il costruttore
c1.number_of_doors = 2 # E' una variabile di classe, di istanza, oppure ... ?

pass