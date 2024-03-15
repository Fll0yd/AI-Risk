import random
import time

class RiskGame:
    def __init__(self, players):
        self.players = players
        self.trade_in_count = 0
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
        self.adjacency_map = {...}  # Initialize the game map with adjacency information
        self.player_cards = {player: [] for player in players}
        self.continents = {
            'North America': ['Alaska', 'Alberta', 'Central America', 'Eastern United States', 'Greenland', 'Northwest Territory', 'Ontario', 'Quebec', 'Western United States'],
            'South America': ['Argentina', 'Brazil', 'Peru', 'Venezuela'],
            'Europe': ['Great Britain', 'Iceland', 'Northern Europe', 'Scandinavia', 'Southern Europe', 'Ukraine', 'Western Europe'],
            'Africa': ['Congo', 'East Africa', 'Egypt', 'Madagascar', 'North Africa', 'South Africa'],
            'Asia': ['Afghanistan', 'China', 'India', 'Irkutsk', 'Japan', 'Kamchatka', 'Middle East', 'Mongolia', 'Siam', 'Siberia', 'Ural', 'Yakutsk'],
            'Australia': ['Eastern Australia', 'Indonesia', 'New Guinea', 'Western Australia']
        }
        self.continent_values = {
            'North America': 5,
            'South America': 2,
            'Europe': 5,
            'Africa': 3,
            'Asia': 7,
            'Australia': 2
        }
        self.connections = {
            'Alaska': ['Alberta', 'Northwest Territory', 'Kamchatka'],
            'Alberta': ['Alaska', 'Northwest Territory', 'Ontario', 'Western United States'],
            'Central America': ['Eastern United States', 'Western United States', 'Venezuela'],
            'Eastern United States': ['Central America', 'Western United States', 'Quebec', 'Ontario'],
            'Greenland': ['Northwest Territory', 'Quebec', 'Iceland'],
            'Northwest Territory': ['Alaska', 'Alberta', 'Ontario', 'Greenland'],
            'Ontario': ['Northwest Territory', 'Alberta', 'Western United States', 'Eastern United States', 'Quebec'],
            'Quebec': ['Ontario', 'Eastern United States', 'Greenland'],
            'Western United States': ['Alberta', 'Ontario', 'Eastern United States', 'Central America'],
            'Argentina': ['Brazil', 'Peru'],
            'Brazil': ['Argentina', 'Peru', 'Venezuela', 'North Africa'],
            'Peru': ['Argentina', 'Brazil', 'Venezuela'],
            'Venezuela': ['Central America', 'Brazil', 'Peru'],
            'Great Britain': ['Iceland', 'Northern Europe', 'Scandinavia', 'Western Europe'],
            'Iceland': ['Greenland', 'Great Britain', 'Scandinavia'],
            'Northern Europe': ['Great Britain', 'Scandinavia', 'Southern Europe', 'Ukraine', 'Western Europe'],
            'Scandinavia': ['Iceland', 'Great Britain', 'Northern Europe', 'Ukraine'],
            'Southern Europe': ['Western Europe', 'Northern Europe', 'Ukraine', 'Middle East', 'Egypt', 'North Africa'],
            'Ukraine': ['Scandinavia', 'Northern Europe', 'Southern Europe', 'Middle East', 'Afghanistan', 'Ural'],
            'Western Europe': ['Great Britain', 'Northern Europe', 'Southern Europe', 'North Africa'],
            'Congo': ['North Africa', 'East Africa', 'South Africa'],
            'East Africa': ['Egypt', 'North Africa', 'Congo', 'South Africa', 'Madagascar', 'Middle East'],
            'Egypt': ['Southern Europe', 'Middle East', 'East Africa', 'North Africa'],
            'Madagascar': ['East Africa', 'South Africa'],
            'North Africa': ['Brazil', 'Western Europe', 'Southern Europe', 'Egypt', 'East Africa', 'Congo'],
            'South Africa': ['Congo', 'East Africa', 'Madagascar'],
            'Afghanistan': ['Ural', 'China', 'India', 'Middle East', 'Ukraine'],
            'China': ['Ural', 'Siberia', 'Mongolia', 'Siam', 'India', 'Afghanistan'],
            'India': ['Middle East', 'Afghanistan', 'China', 'Siam'],
            'Irkutsk': ['Siberia', 'Yakutsk', 'Kamchatka', 'Mongolia'],
            'Japan': ['Mongolia', 'Kamchatka'],
            'Kamchatka': ['Yakutsk', 'Irkutsk', 'Mongolia', 'Japan', 'Alaska'],
            'Middle East': ['Ukraine', 'Afghanistan', 'India', 'East Africa', 'Egypt', 'Southern Europe'],
            'Mongolia': ['Siberia', 'Irkutsk', 'Kamchatka', 'Japan', 'China'],
            'Siam': ['India', 'China', 'Indonesia'],
            'Siberia': ['Ural', 'Yakutsk', 'Irkutsk', 'Mongolia', 'China'],
            'Ural': ['Ukraine', 'Afghanistan', 'China', 'Siberia'],
            'Yakutsk': ['Siberia', 'Irkutsk', 'Kamchatka'],
            'Eastern Australia': ['Western Australia', 'New Guinea'],
            'Indonesia': ['Siam', 'New Guinea', 'Western Australia'],
            'New Guinea': ['Indonesia', 'Western Australia', 'Eastern Australia'],
            'Western Australia': ['Indonesia', 'New Guinea', 'Eastern Australia']
        }

    def generate_cards(self):
        types = ['Infantry', 'Cavalry', 'Artillery']
        cards = [{'territory': territory, 'type': types[i % len(types)]} for i, territory in enumerate(self.territories.keys())]
        random.shuffle(cards)
        return cards                    

    def trade_cards_for_troops(self, player):
        if len(self.player_cards[player]) >= 3:
            types = [card['type'] for card in self.player_cards[player][:3]]
            territories = [card['territory'] for card in self.player_cards[player][:3]]
            if len(set(types)) == 1 or len(set(types)) == 3:  # Check if the first three cards are either all the same type or all different types
                self.player_cards[player] = self.player_cards[player][3:]
                self.trade_in_count += 1
                bonus_troops = max(4, self.trade_in_count * 2)  # The number of troops received depends on the number of sets traded in so far in the game
                if all(territory in self.players[player] for territory in territories):  # Check if the player owns all of the territories on the cards
                    bonus_troops += 2  # Add 2 bonus troops
                return bonus_troops
        return 0

    def generate_game_map(self):
        # Generate a dictionary representing adjacency information for each territory
        game_map = {}
        for territory in self.territories:
            game_map[territory] = [adjacent_territory for adjacent_territory in self.adjacency_map[territory]]
        return game_map

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
        while num_armies > 0:
            for player in self.players:
                territories_owned = self.players[player]
                for territory in territories_owned:
                    if num_armies > 0:
                        self.territories[territory]['troops'] += 1
                        num_armies -= 1
                        
    def start_game(self):
        print("Distributing territories...")
        time.sleep(1)
        self.distribute_territories()
        print("Placing initial armies...")
        time.sleep(1)
        self.place_initial_armies()
        print("Starting game...")
        while True:
            # Rotate the players list to simulate a clockwise turn order
            self.players = self.players[1:] + self.players[:1]
            for player in self.players:
                for player in list(self.players.keys()):
                    if player in self.players:  # Check if the player has not been eliminated
                        print(f"Player {player}'s turn")
                        # Trade in cards at the start of the turn if player has 5 or more cards
                        while len(self.player_cards[player]) >= 5:
                            self.trade_cards_for_troops(player)
                        self.reinforce_territories(player)
                        self.reinforce_territories(player)
                        conquered = self.attack_phase(player)
                        # Trade in cards after attack phase if player has 5 or more cards
                        while len(self.player_cards[player]) >= 5:
                            self.trade_cards_for_troops(player)
                        if conquered:
                            print(f"Player {conquered} has won the game!")
                            return
                        self.fortify_phase(player)
                        # Trade in cards after fortify phase if player has 5 or more cards
                        while len(self.player_cards[player]) >= 5:
                            self.trade_cards_for_troops(player)
                        # If the player has conquered a territory and there are cards left, give them a card
                        if self.cards and conquered:
                            self.player_cards[player].append(self.cards.pop())

    def ai_turn(self, player):
        print(f"AI Player {player}'s turn")
        time.sleep(1)
        print(f"AI Player {player} is trading cards for troops...")
        time.sleep(1)
        extra_troops = self.trade_cards_for_troops(player)
        print(f"AI Player {player} is receiving continent bonus troops...")
        time.sleep(1)
        extra_troops += self.continent_bonus(player)
        print(f"AI Player {player} is receiving territory bonus troops...")
        time.sleep(1)
        territories_owned = self.players[player]
        extra_troops += max(len(territories_owned) // 3, 3)
        print(f"AI Player {player} is deploying troops...")
        time.sleep(1)
        # Trade in cards at the start of the turn if AI player has 5 or more cards
        while len(self.player_cards[player]) >= 5:
            self.trade_cards_for_troops(player)
        # Reinforce territories adjacent to enemy territories, prioritizing those with a numerical disadvantage
        territories_to_reinforce = sorted([t for t in territories_owned if self.get_neighboring_enemy_territories(t)], key=lambda t: self.territories[t]['troops'])
        for _ in range(extra_troops):
            territory = territories_to_reinforce.pop(0)
            self.territories[territory]['troops'] += 1
        print(f"AI Player {player} has placed {extra_troops} troops on their territories.")
        print(f"AI Player {player} is attacking...")
        time.sleep(1)
        # Attack from territories where we have a numerical advantage, prioritizing those where the enemy has a numerical disadvantage
        for territory in sorted(territories_owned, key=lambda t: self.territories[t]['troops'], reverse=True):
            enemy_territories = self.get_neighboring_enemy_territories(territory)
            if enemy_territories:
                target_territory = min(enemy_territories, key=lambda t: self.territories[t]['troops'])
                self.attack(territory, target_territory)
        # Trade in cards after attack phase if AI player has 5 or more cards
        while len(self.player_cards[player]) >= 5:
            self.trade_cards_for_troops(player)
        print(f"AI Player {player} is fortifying...")
        time.sleep(1)
        # Move troops from territories not adjacent to enemy territories to territories adjacent to enemy territories, prioritizing those with a numerical disadvantage
        territories_to_fortify_from = [t for t in territories_owned if not self.get_neighboring_enemy_territories(t)]
        territories_to_fortify_to = sorted([t for t in territories_owned if self.get_neighboring_enemy_territories(t)], key=lambda t: self.territories[t]['troops'])
        if territories_to_fortify_from and territories_to_fortify_to:
            source = random.choice(territories_to_fortify_from)
            target = territories_to_fortify_to.pop(0)
            troops_to_move = self.territories[source]['troops'] - 1
            self.territories[source]['troops'] -= troops_to_move
            self.territories[target]['troops'] += troops_to_move
        # Trade in cards after fortify phase if AI player has 5 or more cards
        while len(self.player_cards[player]) >= 5:
            self.trade_cards_for_troops(player)

    def reinforce_territories(self, player):
        territories_owned = [territory for territory in self.territories if self.territories[territory]['owner'] == player]
        extra_troops = max(len(territories_owned) // 3, 3)
        extra_troops += self.trade_cards_for_troops(player)
        # Add continent bonus
        for continent, territories in self.continents.items():
            if all(self.territories[territory]['owner'] == player for territory in territories):
                extra_troops += self.continent_values[continent]
        while extra_troops > 0:
            print(f"You have {extra_troops} troops left to place.")
            territory = input("Enter the name of the territory where you want to place your troops: ")
            if territory not in territories_owned:
                print("Invalid territory. You can only place troops on territories you own.")
                continue
            troops_to_place = int(input("Enter the number of troops you want to place on this territory: "))
            if troops_to_place > extra_troops:
                print("You don't have that many troops left to place.")
                continue
            self.territories[territory]['troops'] += troops_to_place
            extra_troops -= troops_to_place
            
    def attack(self, attacking_teritory, defending_teritory):
        if self.territories[attacking_teritory]['troops'] > 1:
            attacking_troops = min(3, self.territories[attacking_teritory]['troops'] - 1)
            defending_troops = min(2, self.territories[defending_teritory]['troops'])
            attacker_dice = sorted([random.randint(1, 6) for _ in range(attacking_troops)], reverse=True)
            defender_dice = sorted([random.randint(1, 6) for _ in range(defending_troops)], reverse=True)
            for a, d in zip(attacker_dice, defender_dice):
                if a > d:
                    self.territories[defending_teritory]['troops'] -= 1
                else:
                    self.territories[attacking_teritory]['troops'] -= 1
            if self.territories[defending_teritory]['troops'] == 0:
                self.territories[defending_teritory]['owner'] = self.territories[attacking_teritory]['owner']
                while True:
                    troops_to_move = int(input(f"How many troops do you want to move to {defending_teritory}? (Must be between {attacking_troops} and {self.territories[attacking_teritory]['troops'] - 1}): "))
                    if attacking_troops <= troops_to_move <= self.territories[attacking_teritory]['troops'] - 1:
                        break
                    print("Invalid number of troops. Please enter a valid number.")
                self.territories[attacking_teritory]['troops'] -= troops_to_move
                self.territories[defending_teritory]['troops'] += troops_to_move
                self.check_elimination(self.territories[defending_teritory]['owner'])
                return True
        return False

    def check_elimination(self, player):
        if not any(territory['owner'] == player for territory in self.territories.values()):
            print(f"Player {player} has been eliminated!")
            # Transfer cards of the eliminated player to the player who eliminated them
            for p, cards in self.player_cards.items():
                if player in cards:
                    self.player_cards[p].remove(player)
                    self.player_cards[self.territories[player]['owner']].append(player)
            del self.players[player] # Remove the player from the game   

    def attack_phase(self, player):
        territories_owned = self.players[player]
        has_attacked = False
        while True:
            valid_attack_from = [territory for territory in territories_owned if self.territories[territory]['troops'] > 1 and self.get_neighboring_enemy_territories(territory)]
            if not valid_attack_from:
                break
            for territory in valid_attack_from:
                enemy_territories = self.get_neighboring_enemy_territories(territory)
                while enemy_territories:
                    # Ask the player if they want to continue attacking
                    continue_attack = input("Do you want to continue attacking? (yes/no): ")
                    if continue_attack.lower() != 'yes':
                        return has_attacked if not isinstance(has_attacked, str) else False
                    target_territory = max(enemy_territories, key=lambda t: self.territories[territory]['troops'] - self.territories[t]['troops'])
                    while self.territories[territory]['troops'] > 1 and self.territories[target_territory]['owner'] != player:
                        if target_territory in self.connections[territory]:  # Check if the target territory is adjacent to the attacking territory
                            if self.attack(territory, target_teritory, min(3, self.territories[territory]['troops'] - 1)):
                                has_attacked = True
                                winner = self.check_win_condition()
                                if winner:
                                    return winner
                    enemy_territories = [t for t in enemy_territories if self.territories[t]['owner'] != player and t in self.connections[territory]]  # Only consider territories that are connected to the current territory and owned by other players
        return has_attacked if not isinstance(has_attacked, str) else False

    def fortify(self, source, target):
        max_troops_to_move = self.territories[source]['troops'] - 1
        if max_troops_to_move > 0:
            while True:
                try:
                    troops_to_move = int(input(f"How many troops do you want to move from {source} to {target}? (Must be between 1 and {max_troops_to_move}): "))
                    if 1 <= troops_to_move <= max_troops_to_move:
                        break
                    print("Invalid number of troops. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            self.territories[source]['troops'] -= troops_to_move
            self.territories[target]['troops'] += troops_to_move
            
    def is_connected(self, source, target, player):
        visited = set()

        def dfs(territory):
            if territory == target:
                return True
            if self.territories[territory]['owner'] != player or territory in visited:
                return False
            visited.add(territory)
            return any(dfs(neighbour) for neighbour in self.connections[territory] if self.territories[neighbour]['owner'] == player)
        return dfs(source)

    def fortify_phase(self, player):
        fortify_choice = input("Do you want to fortify? Enter 'yes' or 'no': ")
        if fortify_choice.lower() == 'no':
            return  # End the fortify phase if the player chooses not to fortify at all

        territories_owned = self.players[player]
        fortified_pairs = set()  # Keep track of fortified pairs
        for territory in territories_owned:
            friendly_territories = self.get_neighboring_friendly_territories(territory)
            if friendly_territories:
                for target_territory in friendly_territories:
                    # Check if the pair has not been fortified yet and the territories are connected
                    if (territory, target_territory) not in fortified_pairs and self.is_connected(territory, target_territory, player):
                        fortify_choice = input(f"Do you want to fortify {territory} to {target_territory}? Enter 'yes' or 'no': ")
                        if fortify_choice.lower() == 'yes':
                            self.fortify(territory, target_territory)
                            fortified_pairs.add((territory, target_territory))  # Add the pair to the fortified pairs
                        elif fortify_choice.lower() == 'no':
                            return  # End the fortify phase if the player chooses not to continue

    def get_neighboring_enemy_territories(self, territory):
        return [t for t in self.connections[territory] if self.territories[t]['owner'] != self.territories[territory]['owner']]

    def get_neighboring_friendly_territories(self, territory):
        return [t for t in self.connections[territory] if self.territories[t]['owner'] == self.territories[territory]['owner']]

    def check_win_condition(self):
        if len(set(territory['owner'] for territory in self.territories.values())) == 1:
            return next(iter(self.players))
        return None

players = ['AI Red', 'AI Blue', 'AI Green', 'AI Yellow', 'AI Black']
players_territories = {player: [] for player in players}

risk_game = RiskGame(players_territories)
risk_game.start_game()