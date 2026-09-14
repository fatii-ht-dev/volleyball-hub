players = []


def add_player():
    name = input("Player name: ")
    position = input("Player position: ")
    player = {
        "name" : name,
        "position" : position
    }

    players.append(player)

def show_player():
    if not players:
        print("Oops! The player not found!")
        return

    print("\nPlayers: ")

    for number, player in enumerate(players, start=1):
        print(f"{number}.{player['name']} - {player['position']}")

while True:
    print("\n---Players Management---")
    print("1. Add player")
    print("2. Show player")
    print("3. Exit")

    choise = input("Coise an option: ")

    if choise == "1":
        add_player()

    elif choise == "2":
        show_player()

    elif choise == "3":
        print("See you later, Volleyball player!💕")
        break

    else:
        print("Invalid choice.")
