from game.card import Card

class Director:
    """The player who is playing the game.
    
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        points (int): The current points of the player.
        cards (List[Card]): A list of Card instances.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        
        self.points = 300
        
        self.cards = []
        
        # Create 13 Card objects and append them to the cards list
        for i in range(13):
            self.cards.append(Card())

    def start_game(self):
        pass
       
