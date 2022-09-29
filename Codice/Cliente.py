class Cliente:
    # param nome: deve essere una stringa, contenere dei caratteri (no numeri, no caratteri speciali, solo lettere)
    # param cognome: deve essere una stringa, contenere dei caratteri (no numeri, no caratteri speciali, solo lettere)
    # param IBAN: stringa di 27 caratteri (no caratteri speciali)

    def __init__(self, nome, cognome, iban):
        self.__nome = nome
        self.__cognome = cognome
        self.__iban = iban



    def setNome(self, nome):
        if (len(nome) > 20) or (len(nome) < 2):  # lunghezza da 2 a 20
           raise(ValueError("la lunghezza del nome non è corretta"))
           return
        if any((c < "A" or c > "z") for c in nome):  # solo lettere
            raise (ValueError("Il nome può contenere solo lettere non caratteri speciali"))
            return
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCognome(self, cognome):
        if (len(cognome) > 20) or (len(cognome) < 2):
           raise (ValueError("la lunghezza del nome non è corretta"))
           return
        if any((c < "A" or c > "z") for c in cognome):
           raise (ValueError("Il nome può contenere solo lettere non caratteri speciali"))
           return
        self.__cognome = cognome

    def getCognome(self):
        return self.__cognome

    def setIban(self, iban):
        if len(iban) == 27 : #lunga 27 caratteri
           raise (ValueError("la lunghezza della matricola è di 27 caratteri"))
           return
        if not((c < "A" or c > "z") for c in iban):
           raise (ValueError("Matricola non contiene caratteri speciali"))
           return
        self.__iban = iban

    def getIban(self):
        return self.__iban


    def datiCliente(self):
        str_ret = "Sig/Sig.ra " + self.__nome + " " + self.__cognome
        str_ret += "\nIBAN: " + self.__iban + "\n"
        return str_ret

class Conto:
    def __init__(self, IBAN: str, cliente: Cliente):
         self.__IBAN = IBAN
         self.__cliente = {}
         self.addcliente(cliente)

    def getCliente(self):
        return self.__cliente

    def addCliente(self, cliente):
        self.getCliente() = cliente

    @property
    def IBAN(self):
        return self.__IBAN

    def estrattoconto(self):
        estratto = "Transazioni "
        estratto += "----------"
        return estratto

class App_eporfoglio:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_conti = {}
        self.lista_clienti = {}

    @property
    def nome(self):
    return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome





