#Kostantinos-Andrianos Kossyvakis
#4294
import random

# Διαστάσεις ταμπλό 5x5
ROWS = ['a', 'b', 'c', 'd', 'e']
COLS = ['1', '2', '3', '4', '5']

# Κάθε παίκτης έχει 5 πλοία
NUMBER_OF_SHIPS = 5


# Μετατρέπει μια θέση σε "κανονική" μορφή:
# αφαιρεί κενά και κάνει τα γράμματα πεζά.
def normalize_position(pos):
    return pos.strip().lower()


# Ελέγχει αν μια θέση είναι έγκυρη, π.χ. a1, c4, e5.
def valid_position(pos):
    pos = normalize_position(pos)
    return len(pos) == 2 and pos[0] in ROWS and pos[1] in COLS


# Παράγει μια τυχαία θέση του ταμπλό.
def random_position():
    row = ROWS[random.randint(0, 4)]
    col = COLS[random.randint(0, 4)]
    return row + col


# Ζητά από τον χρήστη να επιλέξει 1-player ή 2-player game.
# Επαναλαμβάνει μέχρι να δοθεί σωστή επιλογή.
def read_game_mode():
    mode = input("Input 1 for 1-player game or 2 for 2-player game: ").strip()
    while mode not in ("1", "2"):
        mode = input("Invalid choice. Please enter 1 or 2: ").strip()
    return mode


# Διαβάζει τις θέσεις των πλοίων ενός ανθρώπινου παίκτη.
# Δεν επιτρέπει άκυρες ή διπλές θέσεις.
def read_ship_positions(player_name):
    ships = []

    for i in range(NUMBER_OF_SHIPS):
        prompt = player_name + " enter the position of your ship no " + str(i + 1) + ": "
        pos = normalize_position(input(prompt))

        while (not valid_position(pos)) or (pos in ships):
            pos = normalize_position(input("Invalid position, or position already taken. Try again: "))

        ships.append(pos)

    return ships


# Δημιουργεί τυχαία τις θέσεις των 5 πλοίων του υπολογιστή.
# Φροντίζει να μην υπάρχουν διπλές θέσεις.
def generate_random_ships():
    ships = []

    while len(ships) < NUMBER_OF_SHIPS:
        pos = random_position()
        if pos not in ships:
            ships.append(pos)

    return ships


# Ζητά από έναν ανθρώπινο παίκτη τη θέση στην οποία θα ρίξει βολή.
# Δεν επιτρέπει άκυρες θέσεις ή θέσεις όπου έχει ήδη ρίξει.
def read_missile_position(player_name, shots):
    pos = normalize_position(input(player_name + " enter the position to throw your missile: "))

    while (not valid_position(pos)) or (pos in shots):
        pos = normalize_position(input("Invalid position, or missile already thrown there. Try again: "))

    return pos


# Επιλέγει τυχαία θέση βολής για τον υπολογιστή,
# αποφεύγοντας θέσεις που έχουν ήδη χρησιμοποιηθεί.
def generate_random_missile(shots):
    pos = random_position()

    while pos in shots:
        pos = random_position()

    return pos


# Δημιουργεί το κείμενο μιας γραμμής του ταμπλό.
# o = επιτυχία, x = αποτυχία, κενό = θέση που δεν έχει χτυπηθεί ακόμα.
def board_row_text(hit_positions, miss_positions, row):
    text = ""

    for col in COLS:
        pos = row + col
        if pos in hit_positions:
            text += "o"
        elif pos in miss_positions:
            text += "x"
        else:
            text += " "

    return text


# Τυπώνει και τα δύο ταμπλό δίπλα-δίπλα.
# Σε κάθε ταμπλό φαίνονται μόνο οι βολές που έχει δεχτεί ο κάθε παίκτης.
def print_boards(player1, player2):
    print(" P1    P2")
    print("  12345 12345")

    for row in ROWS:
        left = board_row_text(player1["hits_received"], player1["misses_received"], row)
        right = board_row_text(player2["hits_received"], player2["misses_received"], row)
        print(row + " " + left + " " + row + " " + right)


# Εκτελεί έναν ολόκληρο γύρο για τον τρέχοντα παίκτη.
# Επιστρέφει True αν μετά τη βολή τελείωσε το παιχνίδι.
def take_turn(attacker, defender, player1, player2):
    # Αν παίζει ο υπολογιστής, η βολή είναι τυχαία.
    # Αλλιώς, ζητάμε θέση από τον χρήστη.
    if attacker["is_computer"]:
        pos = generate_random_missile(attacker["shots"])
    else:
        pos = read_missile_position(attacker["name"], attacker["shots"])

    # Καταγραφή της βολής στις προηγούμενες βολές του παίκτη.
    attacker["shots"].append(pos)
    print("Missile thrown at " + pos)

    # Έλεγχος αν η βολή πέτυχε πλοίο του αντιπάλου.
    if pos in defender["ships"]:
        defender["hits_received"].append(pos)
        print("Target hit!")
    else:
        defender["misses_received"].append(pos)
        print("Target missed!")

    # Εκτύπωση των δύο ταμπλό μετά τη βολή.
    print_boards(player1, player2)

    # Το παιχνίδι τελειώνει όταν ο αμυνόμενος δεχτεί 5 επιτυχίες.
    return len(defender["hits_received"]) == NUMBER_OF_SHIPS


# Δημιουργεί και επιστρέφει μια δομή δεδομένων για έναν παίκτη.
def build_player(name, is_computer, ships):
    return {
        "name": name,
        "is_computer": is_computer,
        "ships": ships,
        "shots": [],
        "hits_received": [],
        "misses_received": []
    }


# Κύρια συνάρτηση του προγράμματος.
# Οργανώνει όλη τη ροή: επιλογή mode, τοποθέτηση πλοίων,
# επιλογή πρώτου παίκτη, εναλλαγή γύρων και τερματισμό παιχνιδιού.
def main():
    print("BATTLESHIP GAME")
    print("The objective is to sink the opponent's ships before the opponent sinks yours.")

    mode = read_game_mode()

    # Ο Player 1 βάζει πάντα πρώτος τα πλοία του.
    player1_ships = read_ship_positions("Player 1")

    # Αν είναι 2-player game, ζητάμε και τα πλοία του Player 2.
    # Αλλιώς τα πλοία του υπολογιστή μπαίνουν τυχαία.
    if mode == "2":
        print("\n" * 30)
        player2_ships = read_ship_positions("Player 2")
        player2_name = "Player 2"
        player2_is_computer = False
    else:
        player2_ships = generate_random_ships()
        player2_name = "CPU"
        player2_is_computer = True

    # Δημιουργία των δύο παικτών.
    player1 = build_player("Player 1", False, player1_ships)
    player2 = build_player(player2_name, player2_is_computer, player2_ships)

    # Επιλογή τυχαίου παίκτη που ξεκινά πρώτος.
    if random.randint(1, 2) == 1:
        attacker = player1
        defender = player2
    else:
        attacker = player2
        defender = player1

    print(attacker["name"] + " starts first")
    print_boards(player1, player2)

    game_over = False

    # Κύριος βρόχος παιχνιδιού: συνεχίζει μέχρι να κερδίσει κάποιος.
    while not game_over:
        game_over = take_turn(attacker, defender, player1, player2)

        if game_over:
            print("GAME OVER. " + attacker["name"] + " wins")
        else:
            # Εναλλαγή ρόλων για τον επόμενο γύρο.
            attacker, defender = defender, attacker


# Εκκίνηση του προγράμματος.
main()
