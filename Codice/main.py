from Cliente import Cliente

# print(s.getNome() + " " + s.getCognome() + " " + s.getMatricola())

if __name__ == '__main__':
    # test nome
    # test 1:
    try:
        c1 = Cliente("Mario", "Rossi", "IT60X0542811101000000123456")
        print("Test 1 passato")
    except ValueError as ve:
        print("Test 1 non passato", ve.args)

    # test 2:
    try:
        c1 = Cliente("M", "Rossi", "IT60X0542811101000000123456")
        print("Test 2 non passato")
    except ValueError as ve:
        print("Test 2 passato", ve.args)

    # test 3:
    try:
        c1 = Cliente("Taumatawhakatangihanga", "Rossi", "IT60X0542811101000000123456")
        print("Test 3 non passato")
    except ValueError as ve:
        print("Test 3 passato", ve.args)

    # test 4:
    try:
        c1 = Cliente("Mario Marco", "Rossi", "12345")
        print("Test 4 non passato")
    except ValueError as ve:
        print("Test 4 passato", ve.args)

    # test 5:
    try:
        c1 = Cliente("Mario 1", "Rossi", "IT60X0542811101000000123456")
        print("Test 5 non passato")
    except ValueError as ve:
        print("Test 5 passato", ve.args)

    # test 6:
    try:
        c1 = Cliente("M@rio", "Rossi", "IT60X0542811101000000123456")
        print("Test 6 non passato")
    except ValueError as ve:
        print("Test 6 passato", ve.args)

    # test cognome
    # test 7:
    try:
        c1 = Cliente("Mario", "Rossi", "IT60X0542811101000000123456")
        print("Test 7 non passato")
    except ValueError as ve:
        print("Test 7 passato", ve.args)

    # test 8:
    try:
        c1 = Cliente("Mario", "R", "IT60X0542811101000000123456")
        print("Test 8 non passato")
    except ValueError as ve:
        print("Test 8 passato", ve.args)

    # test 9:
    try:
        c1 = Cliente("Mario", "Taumatawhakatangihanga", "IT60X0542811101000000123456")
        print("Test 9 non passato")
    except ValueError as ve:
        print("Test 9 passato", ve.args)

    # test 10:
    try:
        c1 = Cliente("Mario", "Rossi Bianchi", "IT60X0542811101000000123456")
        print("Test 10 non passato")
    except ValueError as ve:
        print("Test 10 passato", ve.args)

    # test 11:
    try:
        c1 = Cliente("Mario", "Rossi 1", "IT60X0542811101000000123456")
        print("Test 11 non passato")
    except ValueError as ve:
        print("Test 11 passato", ve.args)

    # test 12:
    try:
        c1 = Cliente("Mario", "Ross!", "IT60X0542811101000000123456")
        print("Test 12 non passato")
    except ValueError as ve:
        print("Test 12 passato", ve.args)

    #IBAN
    # test 13:
    try:
        c1 = Cliente("Mario", "Rossi", "IT60X0542811101000000123456")
        print("Test 13 non passato")
    except ValueError as ve:
        print("Test 13 passato", ve.args)

    # test 14:
    try:
        c1 = Cliente("Mario", "Rossi", "IT60X054281110100000012345")
        print("Test 14 non passato")
    except ValueError as ve:
        print("Test 14 passato", ve.args)

    # test 15:
    try:
        c1 = Cliente("Mario", "Rossi", "IT60 X0542811101000000123456")
        print("Test 15 non passato")
    except ValueError as ve:
        print("Test 15 passato", ve.args)

    # test 16:
    try:
        c1 = Cliente("Mario", "Rossi", "?")
        print("Test 16 non passato")
    except ValueError as ve:
        print("Test 16 passato", ve.args)

    # def get e set
    # test 17:
    c2 = Cliente("Mario", "Rossi", "?")
    if("Rossi" == c2.getCognome()):
       print("Test 17 passato")
    else:
       print("Test 17 non passato")

    # test 18:
    c2 = Cliente("Mario", "Rossi", "12345")
    c2.setCognome("Pinto")
    if (c2.getCognome() == "Pinto"):
        print("Test 18 Passato")
    else:
        print("Test 18 Non passato"+" " +c2.getCognome())

    # test 19:
    c2 = Cliente("Mario", "Rossi", "IT60X0542811101000000123456")
    c2.setCognome("Pinto")
    if (c2.getCognome() == "Pinto"):
       print("Test 19 passato")
    else:
       print("Test 19 non passato" + " " + c2.getCognome())

    # test 20:
    c1 = Cliente("Mario", "Rossi", "IT60X0542811101000000123456")
    try:
        c1.setCognome("P@nto")
        print("Test 20 Non passato")
    except ValueError as ve:
        print("test 20 Passato", ve.args)

    c = Cliente("Serena", "Schincaglia", "IT60X0542811101000000123456")

    print(c.datiCliente())

    print()

