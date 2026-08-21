from database import (
    create_database,
    create_car_in_database,
    get_all_cars_in_database,
    remove_car_from_database,
)

def show_menu():
    print("\n--- Parkering System ---")
    print("1. Tilføj bil")
    print("2. Se alle biler")
    print("3. Slet bil")
    print("q. Quit")


def add_car():
    plate = input("Indtast nummerplade: ")

    try: 
        create_car_in_database(plate)
        print(f"Bilen med nummerplade {plate} er nu parkeret")

    except Exception:
        print("Bilen kunne ikke parkeres")


def show_all_cars():
    cars = get_all_cars_in_database()

    if not cars:
        print("Der er ingen biler parkeret")
        return
    
    print("\n----- Parkerede biler -----")

    for car in cars:
        print(f"Nummerplade: {car['plate']}")
        print(f"Parkeringstidspunkt: {car['created_at']}")
        print()


def remove_car():
    plate = input("Indtast nummerplade for bilen du vil fjerne: ")

    deleted = remove_car_from_database(plate)

    if deleted:
        print(f"Bilen med nummerplade {plate} er fjernet")
    else: 
        print(f"Bilen med nummerplade {plate} blev ikke fundet")


def main():
    create_database()

    while True:
        show_menu()

        choice = input("\nVælg en funktion: ").lower()

        if choice == "1":
            add_car()

        elif choice == "2":
            show_all_cars()

        elif choice == "3":
            remove_car()

        elif choice == "q":
            break

        else:
            print("Ugyldigt valg, Prøv igen")

if __name__ == "__main__":
    main()