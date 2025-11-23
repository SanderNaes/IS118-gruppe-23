print("Konflikt: Silje og Sivert")

# Første valg
svar = input("Ta saken i plenum/individuelle samtaler Overlater saken til HR (1 eller 2): ")

while svar not in ("1", "2"):
    svar = input("Du må velge 1 eller 2: ")

print("Videre går saken til konflikten mellom Jabir og Hamdi.")

# Andre valg
valg2 = input("Ta initiativ og sett opp møte (1) eller avvente løsning (2): ")

while valg2 not in ("1", "2"):
    valg2 = input("Du må velge 1 eller 2: ")

print("Du valgte:", valg2)

# Hvis du valgte 1
if valg2 == "1":
    print("Møte om Jabir og Hamdi sine ideer")

    valg3 = input("Jabir sin løsning (1) eller Hamdi sin løsning (2): ")

    while valg3 not in ("1", "2"):
        valg3 = input("Du må velge 1 eller 2: ")

    # Her legger vi inn den viktige regelen
    if valg3 == "1" and svar == "1":
        print("Beste utfall")  # Bare mulig hvis første valg var 1
    elif valg3 == "1" and svar == "2":
      print("Bra utfall.")
    else:
        print("Bra utfall")

# Hvis du valgte 2
else:
    print("Tidsressurser presser situasjonen for Jabir og Hamdi")

    valg4 = input("Setter opp nødmøte (1) eller fortsett å avvente (2): ")

    while valg4 not in ("1", "2"):
        valg4 = input("Du må velge 1 eller 2: ")

    if valg4 == "1":
        print("Verste utfall")
    else:
        print("Verste utfall")
