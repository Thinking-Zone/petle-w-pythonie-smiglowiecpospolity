import random

pada = random.choice([True, False])
zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n): ").lower() 
    if (odpowiedz == "t" and pada) or (odpowiedz == "n" and not pada):
        print("Zgadłeś! Poprawna odpowiedź.")
        zgaduj = False 
    else:
        print("Niestety, błędna odpowiedź. Spróbuj ponownie!")
