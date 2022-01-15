import random

class Card:
    """A card that represents a value from 1 to 13
   
    Attributes:
        value (int): The value of the card
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        # Set the value of this card to a random number ranging from 1 to 13
        self.value = random.randint(1, 13)