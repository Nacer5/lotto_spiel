import random
def begruessung():
    print("Lass uns doch Lotto spielen. Sobald du keine Lust mehr hast, gib ende ein.")

def lotto_spiel():
    lottozahlen = []
    lottozahlen.extend(range(1,50))
    #print(lottozahlen)
    gewinner_zahlen = random.sample(lottozahlen, 6)
    gewinner_zahlen.sort()
    print(gewinner_zahlen)
    geratene_zahlen =[]
    geratene_zahlen.sort()
    antwort = ()
    while antwort != "ende":
        antwort = input("Nenne mir eine Zahl.")
        if gewinner_zahlen == geratene_zahlen:
            print("Gewonnen!")
        else:
            if antwort in gewinner_zahlen:
                geratene_zahlen.append(antwort)
                print("Super")
            else:
                print("Neuer Versuch.")
    print("Unsere heutigen Lottozahlen sind: \n",geratene_zahlen)
    
def verabschiedung():
    print("Danke fürs spielen. Bye.")

def main():
    begruessung()
    lotto_spiel()
    verabschiedung()


main()