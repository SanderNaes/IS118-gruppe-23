true = "Evaluatorene er begeistret over prototypen og teamet jobber godt sammen."
good = "Protoypen ble ferdig, men evaluatorene er ikke så fornøyde som håpt, deler av teamet holder ikke god kommunikasjon."
bad = "Prototypen ble ikke ferdig i tide og noen sakskonflikter har eskalert til personkonflikter."
bad_path = False
bad_end = False

#Første konflikt
c1_p1 = input("Skal Erling velge Plenum Møte, Individuelle Samtaler eller HR for saken mellom Sivert og Silje? ").lower()
if c1_p1 == "plenum møte":
    print("Erling setter opp et møte i plenum og det kommes frem til et kompromiss.")
elif c1_p1 == "individuelle samtaler":
    print("Erling har samtaler med alle på teamet, og klarer å overbevise Sivert om en mer realistisk versjon av Silje sin løsning.")
elif c1_p1 == "hr":
    bad_end = True #setter dårlig slutt som garantert
    print("HR tar over saken, Erling vet ikke hvordan det kommer til å gå.")
else: 
    print("Restart programmet og skriv det slik som det skrives i spørsmålet. (Det med stor forbokstav.)")
    exit()

#Andre konflikt
c2_p1 = input("For konflikten mellom Hamdi og Jabir skal Erling Sette Opp Møte eller Avvente? ").lower()
if c2_p1 == "sette opp møte":
    print("Erling setter opp møte for å velge en løsning, men valget er splittet så han må.")
elif c2_p1 == "avvente":
    print("Erling avventer situasjonen og håper den forbedrer seg etterhvert.")
    bad_path = True # setter opp for å hoppe til den verre veien
else:
    print("Restart programmet og skriv det slik som det skrives i spørsmålet. (Det med stor forbokstav.)")
    exit()

#Siste valg, den gode veien, men og for garantert dårlig slutt 
if bad_path == False:
    c3_p1 = input("Skal Erling velge Jabir eller Hamdi sin løsning? ").lower()
    if bad_end == True:
        print(bad)
        exit()
    elif c3_p1 == "jabir":
        print(true)
        exit()
    elif c3_p1 == "hamdi":
        print(good)
        exit()
    else:
        print("Restart programmet og bare skriv navnet")
        exit()

#Siste valg, den dårlige veien
elif bad_path == True:
    c3_p2 = input("Skal Erling fortsette å Avvente eller Sette Opp Møte? ").lower()
    if bad_end == True:
        print(bad)
        exit()
    elif c3_p2 == "sette opp møte":
        print(good)
        exit()
    elif c3_p2 == "avvente":
        print(bad)
        exit()
    else:
        print("Restart programmet og skriv det slik som det skrives i spørsmålet. (Det med stor forbokstav.)")
        exit()

