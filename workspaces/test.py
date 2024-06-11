print("Welcome to Hide and Seek: Survivor vs. Killer!")

player1 = input("Player 1, enter your name (Survivor): ")
player2 = input("Player 2, enter your name (Killer): ")

print("\nInstructions:")
print(f"{player1} (Survivor): You must hide from the killer and avoid being found.")
print(f"{player2} (Killer): You must find the survivor and kill them with your knife.")

# Game Loop
while True:
    print("\n--- New Round ---")

    # Survivor's Turn
    print(f"\n{player1}, choose a hiding spot:")
    print("1. Closet")
    print("2. Under the bed")
    print("3. Behind the curtains")
    survivor_choice = input("Enter the number of your hiding spot: ")

    # Killer's Turn
    print(f"\n{player2}, where will you search:")
    print("1. Closet")
    print("2. Under the bed")
    print("3. Behind the curtains")
    killer_choice = input("Enter the number of your search location: ")

    # Check if the killer found the survivor
    if survivor_choice == killer_choice:
        print(f"\n{player2} found {player1} hiding and killed them with the knife!")
        print(f"{player2} wins!")
        break
    else:
        print(f"\n{player2} didn't find {player1}. {player1} survives!")
