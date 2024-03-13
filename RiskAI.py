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
        self.shuffle_and_deal_cards()

    def generate_cards(self):
        cards = ['territory1', 'territory2', 'action1', 'action2'] * len(self.territories)
        return cards

    def generate_game_map(self):
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
                self.territories[territory]['troops'] = random.randint(1, 3)

    def start_game(self):
        while not self.check_win_condition():
            for player in self.players:
                self.ai_turn(player)
        print(f"{self.check_win_condition()} has won the game!")
        for territory, data in self.territories.items():
            print(f"{territory}: {data['owner']} owns it with {data['troops']} troops.")

    def ai_turn(self, player):
        print(f"AI Player {player} is deploying troops...")
        time.sleep(1)
        territories_owned = [territory for territory, data in self.territories.items() if data['owner'] == player]
        if territories_owned:
            num_territories = len(territories_owned)
            total_troops_to_place = num_territories * 3
            troops_per_territory = total_troops_to_place // num_territories
            remaining_troops = total_troops_to_place % num_territories
            for territory in territories_owned:
                self.territories[territory]['troops'] += troops_per_territory
            # Distribute remaining troops randomly among territories
            for _ in range(remaining_troops):
                territory = random.choice(territories_owned)
                self.territories[territory]['troops'] += 1
            print(f"AI Player {player} has placed {total_troops_to_place} troops on their territories.")

    def check_win_condition(self):
        owners = [data['owner'] for territory, data in self.territories.items()]
        for player in self.players:
            if owners.count(player) == len(self.territories):
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
