import pickle
from operator import itemgetter

filename = 'betalinger.pk'

fodboldtur ={}

debt = 4500

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")



def printliste():
    for key, value in fodboldtur.items():
        if value >= debt:
            print(f'{key} har betalt det hele')
        else:
            print(f'{key} har betalt {value} og mangler {debt - value}')
    menu()

def registrering():
    navn = input("Spiller navn \nsådan her gøres det: {Navn Efternavn} \nNavn: ")
    if navn in fodboldtur:
        try:
            penge = input("Indtast dit beløb: ")
            fodboldtur[navn] += float(penge)
            print("Beløb ændret")
        except:
            print("Beløb er ikke et tal")
    else:
        print("Navnet kan ikke findes")
    menu()

def sortinglist():
    sort_fodboldtur = dict(sorted(fodboldtur.items(), key=lambda x: x[1]))
    for top in list(sort_fodboldtur.items())[0:3]:
        print(f'\n{top}')
    menu()

def menu():
    print("MENU \n 1: Print liste \n 2: Afslut program \n 3: Registrer betaling \n 4: sortering")
    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        afslut()
    if (valg == '3'):
        registrering()
    if (valg == '4'):
        sortinglist()


infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

