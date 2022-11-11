import random

class Bracket:
    def __init__(self, players):
        self.players_left = []
        self.players_right = []
        picks = [True, False]
        for player in players:
            if '/' in player:
                [player1, player2] = player.split('/')
                # add gamer to left side of bracket with one randomly chosen character type - pick or random
                gamer_left = Gamer(player1, True)
                self.players_left.append(gamer_left)

                gamer_right = Gamer(player2, True)
                self.players_right.append(gamer_right)
            else:
                pick = random.choice(picks)
                gamer_left = Gamer(player, pick)
                self.players_left.append(gamer_left)

                # add same gamer to right side of bracket with opposite character type
                gamer_right = Gamer(player, not pick)
                self.players_right.append(gamer_right)

            

        random.shuffle(self.players_left)
        random.shuffle(self.players_right)
    
    def shuffle(self):
        random.shuffle(self.players_left)
        random.shuffle(self.players_right)
    
    def __str__(self):
        return ('LEFT SIDE\n'
                f'{self.players_left[0]} v {self.players_left[1]}'
                '\n'
                f'{self.players_left[2]} v {self.players_left[3]}'
                '\n\n'
                'RIGHT SIDE\n'
                f'{self.players_right[0]} v {self.players_right[1]}'
                '\n'
                f'{self.players_right[2]} v {self.players_right[3]}')
        

class Gamer:
    def __init__(self, name, pick):
        self.name = name
        self.pick = pick
    
    def translate_pick(self):
        if self.pick:
            # star
            return '⭐'
        else:
            # question mark
            return '❔'
    
    def __str__(self):
        return self.name + ' ' + self.translate_pick()