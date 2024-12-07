def zbrajanje(num1, num2):
    return num1 + num2

def oduzimanje(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return "Greška: Prvi broj mora biti veći od drugog za oduzimanje."

def mnozenje(num1, num2):
    return num1 * num2

def dijeljenje(num1, num2):
    if num2 == 0:
        return "Greška: Dijeljenje s nulom nije dozvoljeno."
    if num1 < 0 and num2 < 0:  # Ako su oba broja negativna
        return abs(num1) / abs(num2)  # Podijeli apsolutne vrijednosti
    elif num1 > num2:  # Standardni slučaj
        return num1 / num2
    else:
        return "Greška: Prvi broj mora biti veći od drugog za dijeljenje."

def calculator():
    print("Dobrodošli u kalkulator!")
    print("Odaberite operaciju:")
    print("1. Zbrajanje")
    print("2. Oduzimanje")
    print("3. Množenje")
    print("4. Dijeljenje")
    print("5. Sve operacije")

    try:
        choice = int(input("Unesite broj operacije (1/2/3/4/5): "))

        if choice not in [1, 2, 3, 4, 5]:
            print("Nevažeći izbor, pokušajte ponovo.")
            return

        num1 = float(input("Unesite prvi broj: "))
        num2 = float(input("Unesite drugi broj: "))

        if choice == 1:
            print(f"Rezultat zbrajanja: {zbrajanje(num1, num2)}")
        elif choice == 2:
            print(f"Rezultat oduzimanja: {oduzimanje(num1, num2)}")
        elif choice == 3:
            print(f"Rezultat množenja: {mnozenje(num1, num2)}")
        elif choice == 4:
            print(f"Rezultat dijeljenja: {dijeljenje(num1, num2)}")
        elif choice == 5:
            print(f"Rezultat zbrajanja: {zbrajanje(num1, num2)}")
            print(f"Rezultat oduzimanja: {oduzimanje(num1, num2)}")
            print(f"Rezultat množenja: {mnozenje(num1, num2)}")
            print(f"Rezultat dijeljenja: {dijeljenje(num1, num2)}")

    except ValueError:
        print("Pogrešan unos, molimo unesite ispravne brojeve i opcije.")

calculator()
