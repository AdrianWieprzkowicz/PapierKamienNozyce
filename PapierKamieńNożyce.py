import random

def moj_wybor():
    # Funkcja pyta użytkownika o wybór
    while True:  # Pętla, która będzie trwała, dopóki użytkownik nie poda prawidłowego wyboru
        try:
            wybor = int(input("Podaj liczbę reprezentującą twój wybór, 1 -> Papier, 2 -> Kamień, 3 -> Nożyce: "))
            # Sprawdzamy, czy liczba jest w dozwolonym zakresie
            if wybor == 1:
                return "Papier"
            elif wybor == 2:
                return "Kamień"
            elif wybor == 3:
                return "Nożyce"
            else:
                print("Błędny wybór! Wybierz 1, 2 lub 3.")  # Użytkownik podał nieprawidłową liczbę
        except ValueError:
            # Obsługuje sytuację, gdy użytkownik poda coś, co nie jest liczbą
            print("Proszę podać liczbę (1, 2 lub 3).")

def wybor_komputera():
    # Funkcja losuje wybór komputera
    wybor = random.randint(1, 3)
    if wybor == 1:
        return "Papier"
    elif wybor == 2:
        return "Kamień"
    elif wybor == 3:
        return "Nożyce"

def zasady(gracz, komputer):
    # Funkcja porównująca wybory gracza i komputera i decydująca o wyniku
    if komputer == "Kamień" and gracz == "Papier" or komputer == "Nożyce" and gracz == "Kamień" or komputer == "Papier" and gracz == "Nożyce":
        return "Wygrałeś"
    elif gracz == komputer:
        return "Remis"
    else:
        return "Przegrałeś"

def gra():
    while True:
        komputer = wybor_komputera()  # Wybór komputera
        gracz = moj_wybor()  # Wybór gracza
        print(f"Twój wybór: {gracz}")
        print(f"Wybór komputera: {komputer}")
        print(zasady(gracz, komputer))  # Wynik rundy

        # Pytanie, czy gracz chce kontynuować grę
        while True:
            kontynuuj = input("Chcesz zagrać ponownie? (tak/nie): ").lower()
            if kontynuuj == "tak" or kontynuuj == "nie":
                break  # Jeśli użytkownik poda "tak" lub "nie", przechodzimy dalej
            else:
                print("Proszę podać 'tak' lub 'nie'.")  # Obsługuje nieprawidłowe odpowiedzi

        if kontynuuj != "tak":
            print("Dziękujemy za grę!")  # Zakończenie gry
            break

gra()