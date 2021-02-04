import string
import secrets

# -----------------------------------------------------------------------------#
# Autore      : 0v3rFlow
# Descrizione : Semplice generatore password
# -----------------------------------------------------------------------------#

class Password:
    def __init__(self,costruttorePassword):
        self.lunghezza = costruttorePassword[0]
        self.speciali = costruttorePassword[1]

    def generaPassword(self):

# Se è attivo il campo caratteri speciali allora prendo anche quelli
        if self.speciali:
            password_character = string.ascii_letters + string.digits + string.punctuation
        else:
            password_character = string.ascii_letters + string.digits

        password = ''.join(secrets.choice(password_character) for i in range(self.lunghezza))

#        Questo è un altro modo
#        output = ''
#        for i in range(self.lunghezza):
#           output = output + random.choice(password_character)

        return password
            
# Creo la funzione che chiede i caratteri
def modelloPassword():
    lunghezza = input('Inserisci la lunghezza della password. [Consiglio 12] ')
    if not lunghezza:
        lunghezza = 12
    speciali = input('Caratteri speciali ? [Y/N]  ')
    modello = (int(lunghezza), speciali)
    return modello


if __name__ == "__main__":

# costruisco il mio modella per la creazione della password
    modello = modelloPassword()

# crea la mia istanza della classe password
    m1 = Password(modello)

# Lancio il metodo genera password
    password = f"Ecco la tua nuova password: {m1.generaPassword()}"
    print(password)





