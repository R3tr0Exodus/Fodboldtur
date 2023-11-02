import pickle
from operator import itemgetter

filename = 'betalinger.pk'

fodboldtur ={}

debt = 4500

# Gemmer ændringer i .pk filen og derefter lukker programmet
def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")


# Printer en liste ud af alle personer i pickle filen samt, hvad de har betalt og hvad de mangler.
# Dividere total "debt" med mængden af personer i .pk filen
def printliste():
    divide = debt / len(fodboldtur)
    for key, value in fodboldtur.items():
        if value >= divide:
            print(f'{key} har betalt det hele')
        else:
            print(f'{key} har betalt {value}dkk og mangler {divide - value}dkk')
    menu()

# Manuelt lægge/fratrække penge af hver individuelt person
# Skriv deres navn og derefter indtast beløb
def registrering():
    divide = debt / len(fodboldtur)
    navn = input("Spiller navn \nsådan her gøres det: {Navn Efternavn} \nNavn: ")
    if navn in fodboldtur:
        try:
            penge = input("Indtast dit beløb: ")
            fodboldtur[navn] += float(penge)
            print(f'Beløb ændret for {navn} og mangler nu {divide - float(penge)}dkk ')
        except:
            print("Beløb er ikke et tal")
    else:
        print("Navnet kan ikke findes")
    menu()

# Sortere listen til folk der har betalt mindst ligger øverst
# Derefter printer den 3 første på listen og viser hvor meget de har betalt
def sortinglist():
    sort_fodboldtur = dict(sorted(fodboldtur.items(), key=lambda x: x[1]))
    for top in list(sort_fodboldtur.items())[0:3]:
        print(f'\n{top}')
    menu()

# Menuen du starter med at se når du begynder programmet
# Giver dig en liste af muligheder du kan vælge imellem
def menu():
    print("MENU \n "
          "1: Print liste \n "
          "2: Afslut program \n "
          "3: Registrer betaling \n "
          "4: sortering")
    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
    elif (valg == '2'):
        afslut()
    elif (valg == '3'):
        registrering()
    elif (valg == '4'):
        sortinglist()
    else:
        print("Det var ikke et gyldigt input, prøv igen\n")
        menu()

# Åbner og indlæser .pk filen inden den kalder på menu
infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

