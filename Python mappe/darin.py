print("Konflikt: Silje og Sivert")

# Første valg
svar = input("Ta saken i plenum/individuelle samtaler Overlater saken til HR (1 eller 2): ")

while svar not in ("1", "2"):
    svar = input("Du må velge 1 eller 2: ")

print("Videre går saken til konflikten mellom Jabir og Hamdi.")

# Andre valg
dilemma1 = input("Ta initiativ og sett opp møte (1) eller avvente løsning (2): ")

while dilemma1 not in ("1", "2"):
    dilemma1 = input("Du må velge 1 eller 2: ")

print("Du valgte:", dilemma1)

# Hvis du valgte 1
if dilemma1 == "1":
    print("Møte om Jabir og Hamdi sine ideer")

    dilemma2 = input("Jabir sin løsning (1) eller Hamdi sin løsning (2): ")

    while dilemma2 not in ("1", "2"):
        dilemma2 = input("Du må velge 1 eller 2: ")

    # Her legger vi inn den viktige regelen
    if dilemma2 == "1" and svar == "1":
        print("Beste utfall")  # Bare mulig hvis første valg var 1
    elif dilemma2 == "1" and svar == "2":
      print("Bra utfall.")
    else:
        print("Bra utfall")

# Hvis du valgte 2
else:
    print("Tidsressurser presser situasjonen for Jabir og Hamdi")

    dilemma3 = input("Setter opp nødmøte (1) eller fortsett å avvente (2): ")

    while dilemma3 not in ("1", "2"):
        dilemma3 = input("Du må velge 1 eller 2: ")

    if dilemma3 == "1":
        print("Verste utfall")
    else:
        print("Verste utfall")
