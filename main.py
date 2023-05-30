from time import sleep
from os import system, unlink

def main():
    r1 = open('./categorie/R1.txt', 'r')
    r2 = open('./categorie/R2.txt', 'r')
    r3 = open('./categorie/R3.txt', 'r')
    r4 = open('./categorie/R4.txt', 'r')
    r5 = open('./categorie/R5.txt', 'r')

    system('cls')
    print("""Pannello gestione smaltimento rifiuti:
    1) Aggiungi
    2) Mostra
    3) Reset

""")
    comando = int(input("Inserisci il comando da eseguire: "))

    match comando:
        case 1:
            aggiungi(r1, r2, r3, r4, r5)
        case 2:
            mostra()
        case 3:
            reset()
        case _:
            print("Comando non trovato")
            sleep(2)
            main()

    r1.close()
    r2.close()
    r3.close()
    r4.close()
    r5.close()


def aggiungi(r1, r2, r3, r4, r5):
    system('cls')
    prodotto = input("Inserisci il prodotto da inserire: ").lower().capitalize().strip()
    lista = open('rifiuti.txt', 'r+')
    lines = lista.readlines()
    trovato = False

    for i, line in enumerate(lines):
        parti = line.strip().split(';')
        if prodotto == parti[1]:
            trovato = True
            quantita = int(parti[0])
            quantita += 1
            line = f"{quantita};{prodotto};{parti[2]}\n"
            lines[i] = line
            break

    if trovato:
        print(f"Prodotto trovato\nQuesto prodotto appartiene al gruppo {parti[2]}")
    else:

        if prodotto in r1.read().split('\n'):
            print("Questo prodotto appartiene al gruppo R1")
            line = f"1;{prodotto};R1\n"
            lines.append(line)
        elif prodotto in r2.read().split('\n'):
            print("Questo prodotto appartiene al gruppo R2")
            line = f"1;{prodotto};R2\n"
            lines.append(line)
        elif prodotto in r3.read().split('\n'):
            print("Questo prodotto appartiene al gruppo R3")
            line = f"1;{prodotto};R3\n"
            lines.append(line)
        elif prodotto in r4.read().split('\n'):
            print("Questo prodotto appartiene al gruppo R4")
            line = f"1;{prodotto};R4\n"
            lines.append(line)
        elif prodotto in r5.read().split('\n'):
            print("Questo prodotto appartiene al gruppo R5")
            line = f"1;{prodotto};R5\n"
            lines.append(line)
        else:
            print("Prodotto non trovato")

    lista.seek(0)
    lista.truncate()
    lista.writelines(lines)
    lista.close()

    input("Premi INVIO per continuare...")
    main()


def mostra():
    lista = open('rifiuti.txt', 'r')
    system('cls')
    print("Lista dei prodotti inseriti:\n")
    
    for line in lista:
        parti = line.strip().split(';')
        print(f"""    Prodotto --> {parti[1]}
    Quantità --> {parti[0]}
    Categoria --> {parti[2]}
        """)

    lista.close()
    input("\nPremi INVIO per continuare...")
    main()


def reset():
    unlink('rifiuti.txt')
    open('rifiuti.txt', 'w').close()
    print("File resettato correttamente")
    input("Premi INVIO per continuare...")
    main()

main()
