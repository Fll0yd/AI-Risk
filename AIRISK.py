import random
import time

class RiskGame:
    def __init__(self, players):
        self.players = players
        self.territories = {
            'Alaska': {'owner': None, 'troops': 0},
            'Alberta': {'owner': None, 'troops': 0},
            'Argentina': {'owner': None, 'troops': 0},
            'Brazil': {'owner': None, 'troops': 0},
            'Central America': {'owner': None, 'troops': 0},
            'China': {'owner': None, 'troops': 0},
            'Congo': {'owner': None, 'troops': 0},
            'East Africa': {'owner': None, 'troops': 0},
            'Eastern Australia': {'owner': None, 'troops': 0},
            'Eastern United States': {'owner': None, 'troops': 0},
            'Egypt': {'owner': None, 'troops': 0},
            'Great Britain': {'owner': None, 'troops': 0},
            'Greenland': {'owner': None, 'troops': 0},
            'Iceland': {'owner': None, 'troops': 0},
            'India': {'owner': None, 'troops': 0},
            'Indonesia': {'owner': None, 'troops': 0},
            'Irkutsk': {'owner': None, 'troops': 0},
            'Japan': {'owner': None, 'troops': 0},
            'Kamchatka': {'owner': None, 'troops': 0},
            'Madagascar': {'owner': None, 'troops': 0},
            'Middle East': {'owner': None, 'troops': 0},
            'Mongolia': {'owner': None, 'troops': 0},
            'New Guinea': {'owner': None, 'troops': 0},
            'North Africa': {'owner': None, 'troops': 0},
            'Northern Europe': {'owner': None, 'troops': 0},
            'Northwest Territory': {'owner': None, 'troops': 0},
            'Ontario': {'owner': None, 'troops': 0},
            'Peru': {'owner': None, 'troops': 0},
            'Quebec': {'owner': None, 'troops': 0},
            'Scandinavia': {'owner': None, 'troops': 0},
            'Siam': {'owner': None, 'troops': 0},
            'Siberia': {'owner': None, 'troops': 0},
            'South Africa': {'owner': None, 'troops': 0},
            'Southern Europe': {'owner': None, 'troops': 0},
            'Ukraine': {'owner': None, 'troops': 0},
            'Ural': {'owner': None, 'troops': 0},
            'Venezuela': {'owner': None, 'troops': 0},
            'Western Australia': {'owner': None, 'troops': 0},
            'Western Europe': {'owner': None, 'troops': 0},
            'Western United States': {'owner': None, 'troops': 0},
            'Yakutsk': {'owner': None, 'troops': 0},
        }
        self.cards = self.generate_cards()
        self.game_map = self.generate_game_map()

    def generate_cards(self):
        cards = ['territory1', 'territory2', 'action1', 'action2'] * len(self.territories)
        return cards

    def generate_game_map(self):
        return {territory: None for territory in self.territories}

    def distribute_territories(self):
        distribution_choice = input("How do you want to distribute territories? Enter 'random' for random distribution or 'turns' for taking turns: ")
        if distribution_choice.lower() == 'random':
            self.random_distribution()
        elif distribution_choice.lower() == 'turns':
            self.claim_territories()
        else:
            print("Invalid choice. Defaulting to random distribution.")
            self.random_distribution()

    def random_distribution(self):
        deck = list(self.territories.keys())
        random.shuffle(deck)
        num_players = len(self.players)
        territories_per_player = len(deck) // num_players
        for _ in range(territories_per_player):
            for player in self.players:
                territory = deck.pop(0)
                self.players[player].append(territory)
                self.territories[territory]['owner'] = player

    def claim_territories(self):
        deck = list(self.territories.keys())
        random.shuffle(deck)
        while deck:
            for player in self.players:
                if deck:
                    territory = deck.pop(0)
                    self.players[player].append(territory)
                    self.territories[territory]['owner'] = player

    def place_initial_armies(self):
        initial_armies = {2: 40, 3: 35, 4: 30, 5: 25, 6: 20}
        num_armies = initial_armies[len(self.players)]
        for player in self.players:
            territories_owned = self.players[player]
            for territory in territories_owned:
                if num_armies > 0:
                    self.territories[territory]['troops'] += 1
                    num_armies -= 1

    def start_game(self):
        self.distribute_territories()
        self.place_initial_armies()

        while not self.check_win_condition():
            for player in self.players:
                self.ai_turn(player)

        print(f"{self.check_win_condition()} has won the game!")
        for territory, data in self.territories.items():
            print(f"{territory}: {data['owner']} owns it with {data['troops']} troops.")

    def ai_turn(self, player):
        print(f"AI Player {player} is deploying troops...")
        time.sleep(1)
        territories_owned = self.players[player]
        num_territories = len(territories_owned)
        total_troops_to_place = num_territories // 3
        for _ in range(total_troops_to_place):
            territory = random.choice(territories_owned)
            self.territories[territory]['troops'] += 1
        print(f"AI Player {player} has placed {total_troops_to_place} troops on their territories.")

        print(f"AI Player {player} is attacking...")
        time.sleep(1)
        for territory in territories_owned:
            enemy_territories = self.get_neighboring_enemy_territories(territory)
            if enemy_territories:
                self.attack(territory, random.choice(enemy_territories))

        print(f"AI Player {player} is fortifying...")
        time.sleep(1)
        for territory in territories_owned:
            friendly_territories = self.get_neighboring_friendly_territories(territory)
            if friendly_territories:
                self.fortify(territory, random.choice(friendly_territories))

    def attack(self, from_territory, to_territory):
        if self.territories[from_territory]['troops'] > 1:
            self.territories[from_territory]['troops'] -= 1
            if self.territories[to_territory]['troops'] == 0:
                self.territories[to_territory]['owner'] = self.territories[from_territory]['owner']
                self.territories[to_territory]['troops'] = 1

    def fortify(self, from_territory, to_territory):
        if self.territories[from_territory]['troops'] > 1:
            self.territories[from_territory]['troops'] -= 1
            self.territories[to_territory]['troops'] += 1

    def get_neighboring_enemy_territories(self, territory):
        return [neighbor for neighbor in self.game_map[territory] if self.territories[neighbor]['owner'] != self.territories[territory]['owner']]

    def get_neighboring_friendly_territories(self, territory):
        return [neighbor for neighbor in self.game_map[territory] if self.territories[neighbor]['owner'] == self.territories[territory]['owner']]
    
    def check_win_condition(self):
        for player in self.players:
            territories_owned = self.players[player]
            if len(territories_owned) == len(self.territories):
                return player
        return None

players = {
    'AI Red': [],
    'AI Blue': [],
    'AI Green': [],
    'AI Yellow': [],
    'AI Black': []
}

risk_game = RiskGame(players)
risk_game.start_game()
