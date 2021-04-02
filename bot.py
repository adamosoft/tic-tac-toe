from typing import List, Tuple
from random import choice

def move(list_of_valid_moves: List) -> Tuple:
    """
    Bot picks random valid move
    """
    return choice(list_of_valid_moves)
