from game.card import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        points (int): The current points of the player
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
        
        for i in range(13):
            self.cards.append(Card())
       
