import random
players = {}
leaderboard = {}
dice_values = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
current_player = 1
current_bet_dice_face = 0
current_bet_num_dice = 0
first_turn = True


class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.dice = []
        self.dice_number = 5

    def roll_dice(self):
        self.dice = []
        for i in range(self.dice_number):
            self.dice.append(random.randint(1, 6))

    def prev_player(self):
        if current_player == 1:
            previous_player = len(players)
        else:
            previous_player = current_player - 1
        return previous_player

    def make_bid(self):
        global current_bet_dice_face
        global current_bet_num_dice
        if first_turn == True:
            current_bet_dice_face = 0
            current_bet_num_dice = 0
        while True:
            print("\n---Make a Bid---")
            print(
                "\nMake a bid. If there are at least as many dice in play as the bid, then the bid is correct.")
            print("Bid must be greater than any previous bid (a greater number of the same face OR any number of a higher face).")

            new_dice_face = int(
                input("\nChoose dice FACE. Enter a value (1-6): "))
            if new_dice_face < current_bet_dice_face:
                print("\n** Must enter a dice face that is of equal or higher value **")
            elif new_dice_face == current_bet_dice_face:
                new_num_dice = int(input("\nEnter a NUMBER of dice: "))
                if new_num_dice <= current_bet_num_dice:
                    print("\n** Number of dice must be higher than previous bid **")
                elif new_num_dice > current_bet_num_dice:
                    current_bet_num_dice = new_num_dice
                    break
            elif new_dice_face > current_bet_dice_face:
                current_bet_dice_face = new_dice_face
                new_num_dice = int(input("\nEnter a NUMBER of dice: "))
                current_bet_num_dice = new_num_dice
                break
            print(
                f"\nCurrent bid is {current_bet_num_dice} {dice_values[current_bet_dice_face]}(s)")
        next_turn()

    def challenge_last_bid(self):
        global current_bet_dice_face
        global current_bet_num_dice
        global first_turn
        total_face = 0
        print("\nPlayers' Previous Dice Values")
        for i in players:
            print(players[i].dice)
            for dice in players[i].dice:
                if dice == current_bet_dice_face:
                    total_face += 1
        if current_bet_dice_face > total_face:
            print(
                f"Only {total_face} {dice_values[current_bet_dice_face]}(s) in play.")
            print(
                f"Last bid was wrong. Player {self.prev_player()} loses a die.")
            players[self.prev_player()].dice.pop()
            players[self.prev_player()].dice_number -= 1
        if current_bet_dice_face <= total_face:
            print(
                f"{total_face} {dice_values[current_bet_dice_face]}(s) in play.")
            print(
                f"Last bid was correct. Player {current_player} loses a die.")
            players[current_player].dice.pop()
            players[current_player].dice_number -= 1
        print("\nPlayers' Current Dice Values")
        for i in players:
            print(players[i].dice)
        print(f"{players[current_player].dice_number} dice left")
        next_turn()
        first_turn = True

    def declare_spot_on(self):
        global current_bet_dice_face
        global current_bet_num_dice
        global first_turn
        total_face = 0
        for i in players:
            print(players[i].dice)
            for dice in players[i].dice:
                if dice == current_bet_dice_face:
                    total_face += 1
        print(f"{total_face} {dice_values[current_bet_dice_face]}(s) in play.")
        if current_bet_num_dice == total_face:
            if players[current_player].dice_number == 5:
                print(
                    "Bid was spot on, but you cannot gain a die, because you have five already. ")
            else:
                print(f"Bid was spot on! Player {current_player} gains a die.")
                players[current_player].dice.append(random.randint(1, 6))
                players[current_player].dice_number += 1
        elif current_bet_num_dice != total_face:
            print(f"Bid was not spot on. Player {current_player} loses a die.")
            players[current_player].dice.pop()
            players[current_player].dice_number -= 1
        next_turn()
        first_turn = True


def main_menu():
    while True:
        global players
        print("\n|------------------------------------|")
        print("|------------LIAR'S DICE-------------|")
        print("|------------------------------------|")
        print("1) Play a Game")
        print("2) Read Rules")
        print("3) View Scores")
        print("4) Exit Game")
        choice = input("\nEnter your choice: ")
        if int(choice) == 1:
            num_players = int(input("Choose number of players (1-5): "))
            for num in range(1, num_players + 1):
                players[num] = Player(num)
    # Prints the key, and the player_number attribute of the value (Player object) for the key-value pairs in 'players'
            print("\nPlayers:")
            for i in players:
                print(players[i].player_number)
            break

        elif int(choice) == 2:
            print("""
                                     --- Rules---

            Liar's Dice is a dice game of cunning and deception. Each player begins
            with 5 dice, which are rolled at the start of each round. The player
            with the first turn will make a starting bid of a quantity of dice faces
            (for example, 3 'threes', 2 'fours', 6 'ones') in play. Then it is the
            next player's turn, who has 3 options:

            1.Make a New Bid

            The player makes a bid that must be greater than the previous bid.
            So it can be an equal number of the same face or any number of a
            higher face.

            2. Challenge Last Bid

            The player may choose to challenge the previous bid. As long as
            the bid was for a equal or lesser amount of dice than are in play,
            it is correct. If the bid exceeded the amount of dice in play, then
            it is incorrect. If the player who made that bid loses a die.
            If the bid was correct, then the player who challenged losed a die.
            Then, a new round begins and all players' dice are rerolled.

            3. Declare Last Bid Spot On

            The player (or 'caller') may declare that the last bid was 'spot on'.
            If the bid was exactly right, the caller gains a die. If the bid was
            not exactly right, the caller loses a die. Then a new round begins and
            all players' dice are rerolled.

            Excitement buils as each player must make a higher bid than the last, and
            they eventually have to start lying, and other players have the chance
            to challenge them! And watchful players have the chance to gain a die, if
            they can guess that the exact amount was bid.

            Play continues until only one player is left with any dice. The last
            player wins!""")

        elif int(choice) == 3:
            if leaderboard == {}:
                print("\nThere are no scores to display yet.")
            else:
                print("          -- Scores --            ")
                print("\n  Player                Wins",)
                for player, score in leaderboard.items():
                    print(" Player {}                 {}".format(player, score))

        elif int(choice) == 4:
            print("Goodbye!")
            exit()


def turn_menu():
    if first_turn == True:
        for i in players:
            players[i].roll_dice()
    print(f"\n-- Player {current_player}'s Turn --")
    if first_turn == False:
        print(
            f"Current bid is {current_bet_num_dice} {dice_values[current_bet_dice_face]}(s)")
    print(f"Total dice: {total_dice()}")
    print("Your Dice: ", players[current_player].dice)
    print("\n1) Bid")
    if first_turn == False:
        print("2) Challenge last bid")
        print("3) Declare last bid spot on")
    choice = input("\nChoose an option: ")
    if int(choice) == 1:
        players[current_player].make_bid()
    if int(choice) == 2:
        players[current_player].challenge_last_bid()
    if int(choice) == 3:
        players[current_player].declare_spot_on()


def next_turn():
    global current_player
    global first_turn
    global leaderboard
    for i in list(players):
        if len(players[i].dice) == 0:
            del players[i]
    if len(players) == 1:
        winning_player = list(players.keys())[0]
        print(
            f"\nPlayer {winning_player} is the only one with dice remaining.")
        print(f"\n\nPlayer {winning_player} is the winner!")
        if winning_player not in leaderboard:
            leaderboard[winning_player] = 1
        elif winning_player in leaderboard:
            leaderboard[winning_player] += 1

    if first_turn == True:
        first_turn = False
    current_player += 1
    if current_player > len(players):
        current_player = 1


def total_dice():
    total = 0
    for player in players:
        total += len((players[player].dice))
    return total


while True:
    main_menu()
    while len(players) > 1:
        turn_menu()
