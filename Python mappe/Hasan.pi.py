print("Du er Erling. Du må ta tre valg.\n")

# Valg 1
valg1 = input("1) Silje og Sivert krangler. A = Du snakker med dem, B = HR tar det: ").upper()

# Valg 2
valg2 = input("2) Hamdi og Jabir er uenige. A = Du setter opp møte, B = Du venter: ").upper()
if valg2 == "A":
    valg3 = input("3) Teamet trenger løsning. A = Kompromiss, B = La en vinne: ").upper()
    if valg1 == "A" and valg3 == "A":
        print("BESTE UTFALL: Teamet leverer, samarbeidet blir bedre.")
    elif valg1 == "A" and valg3 == "B":
        print("BRA UTFALL: Prototypen blir ferdig, men samarbeid kunne vært bedre")
    elif valg1 == "B" and valg3 == "A":
        print("DÅRLIG UTFALL: Prototypen blir ikke ferdig.")
    elif valg1 == "B" and valg3 == "B":
        print("DÅRLIG UTFALL: Prototypen blir ikke ferdig.")
    else:
        print("Feil tast! Velg enten A eller B.")
    
elif valg2 == "B":
    valg4 = input("3) Det er lite tid igjen. A = nødmøte, B = fortsette å vente: ").upper()
    if valg1 == "A" and valg4 == "A":
        print("BRA UTFALL: Prototypen blir ferdig, men samarbeid kunne vært bedre")
    elif valg1 == "A" and valg4 == "B":
        print("DÅRLIG UTFALL: Prototypen blir ikke ferdig.")
    elif valg1 == "B" and valg4 == "A":
        print("DÅRLIG UTFALL: Prototypen blir ikke ferdig.")
    elif valg1 == "B" and valg4 == "B":
        print("DÅRLIG UTFALL: Prototypen blir ikke ferdig.")
    else:
        print("Feil tast! Velg enten A eller B.")
# Valg 3
else:
    print("Feil tast! Velg enten A eller B.")