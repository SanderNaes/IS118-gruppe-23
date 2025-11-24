best = "the project was solved the best way possible, Erling got a promotion."
#den beste løsningen
good = "Project got fisished , but could have gone better"
#prosjektet blir ferdig, men kunne blitt gjort bedre
bad = "project did not finish" 
#prosjektet ble ikke ferdig på grunn av valgene tatt

#dette er første valget.
svar = input("silje and sivert have a dissagreement, do you choose number 1, or 2: ")
if svar == "1":
    svar_1 = input("Dette gitt bra, men sivert er litt trist/begge er ganske fornøyde."
    " nå er Hamdi og Jabir uenige vil du velge løsning 1a eller 2a?: ")
    if svar_1 == "1a":
        svar_2 = input("Erling setter opp møte, erling tar valg, velger du 1c eller 2c?: ")
        if svar_2 == "1c":
            print("erling valgte å støtte Hamdi, dette fører til at prosjektet blir ferdig"
            " dette fører til: " + best)
        elif svar_2 == "2c":
            print("erling valgte å støtte Jabir, dette fører til at prosjektet blir ferdig"
            "Dette fører til: " + good)
        else:
            print("Ugyldig valg, prøv igjen.")

    elif svar_1 == "2a":
        svar_2_1 = input("Setter Erling opp nødmøte: 1, hvis ikke: 2: ")

        if svar_2_1 == "1":
            print("erling avventet løsning, dette fører til at et nødmøte blir holdt "
                "dette fører til: " + good)
        elif svar_2_1 == "2":
            print("erling valgte å ikke holde nødmøte, dette fører til at prosjektet"
            " ikke blir ferdig. Dette fører til: " + bad)
        else:
            print("Ugyldig valg, prøv igjen.")
    else:
        print("Ugyldig valg, prøv igjen.")



elif svar == "2":
    svar_1b = input("Hr slet litt me å løse problemet, nå er Hamdi og Jabir uanige "
    "vil du velge løsning 1b eller 2b?: ")
    if svar_1b == "1b":
        print("Erling velger å avvente, han håper det løser seg selv, dette fører til: "
              + bad)

    elif svar_1b == "2b":
        print("Erling velger jabir, eller Hamdi sin løsning, desverre gjør silje og sivert"
        " sin konflikt at prosjektet ikke blir ferdig, og dermed: " + bad)
    
    else:
        print("Ugyldig valg, prøv igjen.")

else:
    print("Ugyldig valg, prøv igjen.")
