import random
import time

print("==============================")
print(" HET GEHEIME GETAL")
print("==============================")
print("Welkom bij mijn zelfgemaakte game!")
print()

naam = input("Wat is je naam? ")
print("Veel succes,", naam)

score = 0
rondes = 5

for ronde in range(1, rondes + 1):
    print()
    print("------------------------------")
    print("RONDE", ronde)
    print("------------------------------")

    geheim = random.randint(1, 100)
    pogingen = 7
    geraden = False

    print("Ik denk aan een getal tussen 1 en 100.")

    while pogingen > 0:
        try:
            gok = int(input("Wat is je gok? "))
        except ValueError:
            print("Geef een geldig getal in!")
            continue

        if gok < 1 or gok > 100:
            print("Kies een getal tussen 1 en 100!")
            continue

        if gok == geheim:
            print("SUPER! Je hebt het juist!")
            score += pogingen * 10
            geraden = True
            break

        elif gok < geheim:
            print("Hoger!")
        else:
            print("Lager!")

        pogingen -= 1
        print("Pogingen over:", pogingen)

    if not geraden:
        print("Helaas! Het getal was", geheim)

    time.sleep(1)

print()
print("==============================")
print(" EINDSCORE")
print("==============================")
print("Speler:", naam)
print("Score:", score)

if score >= 200:
    print("GEWELDIG GESPEELD!")
elif score >= 100:
    print("Goed gedaan!")
else:
    print("Blijf oefenen!")

print()
print("Bedankt om te spelen!")
print("==============================")
