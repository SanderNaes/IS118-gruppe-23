print ("Erling sitt spill for konflikthåndtering\n")
print ("Du spiller som prosjektlederen Erling i dette spillet\n")
print ("Det har oppstått utfordringer innad i prosjektet, og laget velger derfor å ha et møte for å diskutere\n")
print ("Du går igjennom 3 ulike scenarioer, hvor du må velge hvordan konfliktene må håndteres\n")
print ("Skriv A eller B for å velge svar i de ulike scenarioene\n")
print ("Er du klar for å starte?\n")

svar = input("Skriv ja eller nei for å kunne starte spillet").upper()

if svar == "ja":
    print ("Nydelig! Spillet starter nå\n")
elif svar == "nei":
    print ("Det går fint, spillet er alltid åpent for deg\n")
else:
    print ("Ugyldig svar, skriv vennligst ja eller nei\n")

print ("\n Scenario 1 \n")
print ("Det har oppstått en uenighet mellom to medlemmer av laget, Sivert (IT-rådgiver) og Silje (UX/UI-designer)\n")
print ("Silje mener at løsningen Sivert forslår vil hindre innovasjon og låse brukeropplevelsen\n")
print ("Sivert mener forslaget til Silje er usikkert, urealistisk og for kostbart\n")
print ("Hvordan velger du å håndtere denne konflikten?\n")
Scenario1 =input ("A: Ta individuelle samtaler med alle i laget, spesielt med Sivert og Silje, om hva de synes om saken og hvordan komme til et kompromiss eller om de kan overbevises\nB: Erling kan prøve å ta det opp i plenum og ha gruppene snakke med hverandre mens han medierer\n")
if Scenario1 == "a":
    konflikt = "privat"
    print ("Du velger å ta individuelle samtaler med alle i laget, spesielt Siver og Silje, om hva de synes om saken og hvordan komme til et kompromiss eller om de kan overbevises\n")
elif Scenario1 == "b":
    konflikt = "gruppe"
    print ("Du kan prøve å ta det opp i plenum og ha gruppene snakke med hverandre mens han medierer\n")
else:
    print ("Ugyldig svar, skriv vennligst a eller b\n")

if konflikt == "privat":
    print ("Gjennom samtalene får Erling et godt syn på saken fra begge sider. Ved å gjøre dette kommer han på, med litt hjelp fra dem på siden til Silje, en plan til å gjøre Silje litt forslag litt mer realistisk. Dette er noe Sivert går med på etter Erling har presentert det for han\n")
elif konflikt == "gruppe":
    print ("Ved å ta det opp i plenum, med litt press fra Erling, så kommer laget til et kompromiss som ser mer ut som det Silje ville ha, men som fremdeles kan utvikles innenfor tidsfristen. Sivert og Silje sin kommunikasjon svekkes, men laget holder seg sammen\n")
else:
    print ("Ugyldig svar, skriv vennligst a eller b\n")

print ("\n Scenario 2 \n")
print ("Det har oppstått uenighet mellom to medlemmer av laget, Hamdi (representant fra kulturavdelingen) og Jabir (brukerrepresentant). De er uenige om hvordan innbyggerne skal kunne delta i folkemøter digitalt\n")
print ("Hamdi ønsker å bruke kommunens eksisterende plattform for å få en kontrollert løsning\n")
print ("Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill\n")
print ("Hvordan velger du å håndtere denne konflikten?\n")
Scenario2 =input ("A: Sette opp en privat samtale med begge partene slik at Erling kan forstå begges synspunkt og deretter presentere dette for laget slik at det kan bli gjort en felles avgjørelse\nB: Erling kan avvente uenigheten og håpe at Jabir og Hamdi kommer fram til en løsning på egen hånd\n")
if Scenario2 == "a":
    konflikt = "gruppe"
    print ("Du må ta et valg på hvilket system som skal brukes ettersom at halvparten av laget er enig med Hamdi sin ide, mens den andre halvparten er enig med Jabir sin ide\n")
elif Scenario2 == "b":
    konflikt = "privat"
    print ("Du avventer situasjonen og Hamdi og Jabir forblir uenige og konflikten utvikler seg i de kommende ukene. Du begynner å føle deg tidspresset ettersom at de fremdeles er uenige om en løsning for første prototype\n")
else:
    print ("Ugyldig svar, skriv vennligst a eller b\n")

print ("\n Scenario3 \n")
print ("Motivasjonen og moralen til laget er ikke der den skal være. Konfliktene mellom noen medlemmer av laget har skapt uro hos deg og resten av laget\n")
print ("Hallgeir (politisk rådgiver) ønsker å sette opp et møte med Erling for å diskutere løsninger til å få laget samlet og rolig\n")
print ("Hamdi (representant fra kulturavdelingen) ønsker å ta det opp i plenum med alle i laget slik at alle får si sitt synspunkt og ståsted i konfliktene\n")
print ("Hvordan velger du å håndtere denne konflikten?\n")
Scenario3 =input ("A: Sette opp et møte med Hallgeir for å diskutere løsninger til problemene som har oppstått slik at laget kan samle seg mer og komme på rett spor igjen\nB: Du kan sette opp et møte med laget i plenum slik at alle kan få sagt sitt synspunkt og sammen diskutere en løsning\n")
if Scenario3 == "a":
    konflikt = "privat"
    print ("Du velger å sette opp en individuell samtale med rådgiver Hallgeir for å diskutere løsninger for å samle laget\n")
elif Scenario3 == "b":
    konflikt = "gruppe"
    print ("Du velger å ha et møte med alle i laget slik at alle får sagt det de mener og alle kan komme opp til en løsning sammen\n")
else:
    print ("Ugyldig svar, skriv vennligst a eller b\n")

sak = (Scenario1, Scenario2, Scenario3)
if sak in [("a", "a", "b"), ("b", "a", "b"), ("a", "a", "a")]:
    print ("\n Du håndterte konfliktene på en måte du synes var riktig både individuelt med de i laget og med gruppemøte med laget\n")
elif sak in [("b", "a", "a")]:
    print ("\n Du håndterte konfliktene på en måte som fikk fram samarbeid og forståelse i laget, mens du også tok i bruk rådgiver for å veilede deg til best mulig valg og løsning for laget. Dette førte til at prosjektet ble levert i tidet og laget holder seg sammen\n")
elif sak in [("b", "b", "b"), ("b", "b", "a"), ("a", "b", "b"), ("a", "b", "a")]:
    print ("\n Du valgte, som prosjektleder, å ta beslutninger som førte til at prosjektet ble levert i tidet, men uro blant medlemmer innad i laget fremdeles var tilstedet og irritasjon bygges\n")


print ("\n Takk for at du deltok i spillet! Håper du lærte mer om hvordan man håndterer konflikter og hvordan en prosjektleder sin hverdag kan se ut\n")


          
