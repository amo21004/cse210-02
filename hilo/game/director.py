from game.card import Card

# The player starts the game with 300 points.
# Individual cards are represented as a number from 1 to 13.
# The current card is displayed.
# The player guesses if the next one will be higher or lower.
# The the next card is displayed.
# The player earns 100 points if they guessed correctly.
# The player loses 75 points if they guessed incorrectly.
# If a player reaches 0 points the game is over.
# If a player has more than 0 points they decide if they want to keep playing.
# If a player decides not to play again the game is over.

class Director:
    """Creates the code for the game to run and for what the user
    will input. Start the user's points at 300, display a card, ask user
    if they think the next card will be higher or lower, display the 
    next card, give necessary points, then ask user if they want to keep
    playing. Will continue until user doesn't want to play anymore or
    points are at 0.
    
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        points (int): The current points of the player.
        current card (int): random number between 1 and 13.
        compare card (int): random number between 1 and 13.
        higher lower (string): user picks h or l to compare card one to card two.
        card: instance to call the Card class
    """

    def __init__(self):
        """Constructs a new instance of Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.current_card = 0
        self.is_playing = True
        self.higher_lower = ''
        self.compare_card = 0
        self.points = 300
        self.card = Card()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        Invokes six different methods
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.show_current_card()
            self.higher_lower_input()
            self.show_next_card()
            self.calcualte_points()
            self.play_again_input()
            self.is_over()

    def quit_command(self):
        print()
        print('The game is over!')
        print()
        quit()

    def show_current_card(self):
        """Displays the first individual card (represented as
        a number between 1 and 13).
        
        Args:
            self (Director): an instance of Director.
        """
        self.current_card = self.card.random_card()
        card = self.current_card
        print()
        print(f'The card is: {card}')
        

    def higher_lower_input(self):
        """ Ask the user if they think the next card will 
        be higher or lower than the first.
        
        Args:
            self (Director): an instance of Director.
        """
        self.higher_lower = input('Higher or Lower? [h/l] ')

    def show_next_card(self):
        """Displays the next card (respresented as a number
        between 1 and 13).
        
        Args:
            self (Director): an instance of Director.
        """
        self.compare_card = self.card.random_card()
        next_card = self.compare_card
        print(f'Next card was: {next_card}')
        

    def calcualte_points(self):
        """Takes the users guess and calculates points based
        on whether they were right or not. Points will start
        at 300. 100 points are added if the user guessed 
        correctly, 75 points are taken off if user guesses
        incorrectly. Game stops when points are at 0
        
        Args:
            self (Director): An instance Director."""
        
        if (self.current_card > self.compare_card) and self.higher_lower == 'l':
            self.points += 100
            print(f'Your score is: {self.points}')

        elif (self.current_card < self.compare_card) and self.higher_lower == 'h':
            self.points += 100
            print(f'Your score is: {self.points}')

        elif (self.current_card > self.compare_card) and self.higher_lower == 'h':
            self.points -= 75
            print(f'Your score is: {self.points}')

        elif (self.current_card < self.compare_card) and self.higher_lower == 'l':
            self.points -= 75
            print(f'Your score is: {self.points}')

        else:
            self.points += 0
            print(f'Your score is: {self.points}')

    def is_over(self):
        if self.points <= 0:
            print()
            self.quit_command()

    def play_again_input(self):
        """Ask the user if they want to play again.
        
        Args:
            self (Director): An instance Director.
        """
        if self.points <= 0:
            self.quit_command()
            

        play_again = input('Play again? [y/n] ')
        self.is_playing = (play_again == 'y')
        print()