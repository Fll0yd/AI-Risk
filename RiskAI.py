import random
import time

class RiskGame:
    def __init__(self, players):
        self.players = players
        self.territories = {
            'Alaska': {'owner': None, 'troops': 0},
            'Alberta': {'owner': None, 'troops': 0},
            # Add other territories with their initial owner and troop counts
        }
        self.cards = self.generate_cards()
        self.game_map = self.generate_game_map()
        self.shuffle_and_deal_cards()

    def generate_cards(self):
        # Generate cards representing different territories or actions
        cards = ['territory1', 'territory2', 'action1', 'action2'] * len(self.territories)
        return cards

    def generate_game_map(self):
        # Create an empty game map with territories as keys and None as values
        return {territory: None for territory in self.territories}

    def shuffle_and_deal_cards(self):
        deck = list(self.territories.keys())
        random.shuffle(deck)
        num_players = len(self.players)
        territories_per_player = len(deck) // num_players
        for _ in range(territories_per_player):
            for player in self.players:
                territory = deck.pop(0)
                self.players[player].append(territory)
                self.territories[territory]['owner'] = player
                self.territories[territory]['troops'] = random.randint(1, 3)  # Set random initial troop count

    def start_game(self):
        while not self.check_win_condition():
            for player in self.players:
                self.player_turn(player)
                self.ai_turn(player)
        print(f"{self.check_win_condition()} has won the game!")
        for territory, data in self.territories.items():
            print(f"{territory}: {data['owner']} owns it with {data['troops']} troops.")

    def player_turn(self, player):
        print(f"\n{player}'s turn.")
        territories_owned = [territory for territory, data in self.territories.items() if data['owner'] == player]
        if territories_owned:
            print(f"{player} owns: {', '.join(territories_owned)}")
            action = input(f"{player}, choose an action: place, move, battle, fortify, or end turn: ")
            if action == 'place':
                self.place_troops(player, territories_owned)
            elif action == 'move':
                self.move_troops(player, territories_owned)
            elif action == 'battle':
                self.battle(player, territories_owned)
            elif action == 'fortify':
                self.fortify(player, territories_owned)
            elif action == 'end turn':
                print(f"{player}'s turn has ended.")
            else:
                print("Invalid action. Please choose a valid action.")

    def place_troops(self, player, territories_owned):
        chosen_territory = input(f"{player}, choose a territory to place a troop on: ")
        if chosen_territory in territories_owned:
            self.territories[chosen_territory]['troops'] += 1
            print(f"A troop from {player} has been placed on {chosen_territory}.")
        else:
            print("Invalid territory or you don't own it. Please choose a valid territory.")

    def move_troops(self, player, territories_owned):
        source_territory = input(f"{player}, choose a territory to move troops from: ")
        if source_territory in territories_owned and self.territories[source_territory]['troops'] > 1:
            destination_territory = input(f"{player}, choose a territory to move troops to: ")
            if destination_territory in territories_owned:
                self.territories[source_territory]['troops'] -= 1
                self.territories[destination_territory]['troops'] += 1
                print(f"A troop from {player} has been moved from {source_territory} to {destination_territory}.")
            else:
                print("Invalid destination territory or you don't own it. Please choose a valid territory.")
        else:
            print("Invalid source territory or not enough troops. Please choose a valid territory with at least 2 troops.")

    def battle(self, player, territories_owned):
        source_territory = input(f"{player}, choose a territory to attack from: ")
        if source_territory in territories_owned and self.territories[source_territory]['troops'] > 1:
            destination_territory = input(f"{player}, choose a territory to attack: ")
            if destination_territory in self.territories and self.territories[destination_territory]['owner'] != player:
                if random.randint(1, self.territories[source_territory]['troops']) > random.randint(1, self.territories[destination_territory]['troops']):
                    self.territories[destination_territory]['owner'] = player
                    self.territories[destination_territory]['troops'] = self.territories[source_territory]['troops'] - 1
                    self.territories[source_territory]['troops'] = 1
                    print(f"{player} has won the battle and taken {destination_territory}!")
                else:
                    print(f"{player} has lost the battle.")
            else:
                print("Invalid destination territory or it's owned by you. Please choose a valid enemy territory.")

    def fortify(self, player, territories_owned):
        source_territory = input(f"{player}, choose a territory to fortify: ")
        if source_territory in territories_owned and self.territories[source_territory]['troops'] > 1:
            destination_territory = input(f"{player}, choose a territory to fortify to: ")
            if destination_territory in territories_owned:
                num_troops = int(input(f"{player}, how many troops would you like to fortify? "))
                if num_troops > 0 and num_troops < self.territories[source_territory]['troops']:
                    self.territories[source_territory]['troops'] -= num_troops
                    self.territories[destination_territory]['troops'] += num_troops
                    print(f"{player} has fortified {num_troops} troops from {source_territory} to {destination_territory}.")
                else:
                    print("Invalid number of troops. Please choose a valid number.")
            else:
                print("Invalid destination territory or you don't own it. Please choose a valid territory.")
        else:
            print("Invalid source territory or not enough troops. Please choose a valid territory with at least 2 troops.")

    def ai_turn(self, player):
        print(f"AI Player {player} is deploying troops...")
        time.sleep(1)
        territories_owned = [territory for territory, data in self.territories.items() if data['owner'] == player]
        if territories_owned:
            territory_to_place = random.choice(territories_owned)
            troops_to_place = random.randint(1, 3)
            self.territories[territory_to_place]['troops'] += troops_to_place
            print(f"AI Player {player} has placed {troops_to_place} troops on {territory_to_place}.")

    def check_win_condition(self):
        owners = [data['owner'] for territory, data in self.territories.items()]
        for player in self.players:
            if owners.count(player) == len(self.territories):
                return player
        return None

players = {
    'Red': [],
    'Blue': [],
    'Green': [],
    'Yellow': [],
    'Black': []
}

risk_game = RiskGame(players)
risk_game.start_game()
