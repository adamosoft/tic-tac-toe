from typing import List, Optional


class Tic_tac_toe:


  def __init__(self):

    self.players = {1: "O", 2: "X"}
    self.desk = self.generate_empty(3, 3)
    self.player = 1
    self.winner = None
    self.draw = None


  def run(self) -> None:
    """
    Driven script for console
    """
    done = False
    
    while True:
      if done:
        break
      row = int(input())
      column = int(input())
      if self.player == 1:
        self.desk[row -1][column - 1] = "O"
        if self.evaluate(row -1, column - 1):
          done = True
        self.player = 2
      elif self.player == 2:
        self.desk[row -1][column -1] = "X"
        if self.evaluate(row -1, column - 1):
          done = True
        self.player = 1
      self.print_matrix(self.desk)


  def generate_empty(self, r: int, c: int) -> List:
    """
    Generates a matrix filled with none-value with r-rows and c-columns
    """
    return [[None for i in range(c)] for j in range(r)]


  def print_matrix(self, M: List) -> None:
    """
    Nice print for matrix
    """
    for row in M:
      for column in row:
        if column != None:
          print(f"{column : <5}", end = " ")
        else:
           print(f"{column}", end = " ")

      print()


  # Evaluating possible endings
  def horizontal(self) -> Optional[bool]:
    """
    Evaluates horizontal win
    """
    if self.desk[0][0] == self.desk[0][1] == self.desk[0][2] and self.desk[0][0] != None:
      return True
    if self.desk[1][0] == self.desk[1][1] == self.desk[1][2] and self.desk[1][0] != None:
      return True
    if self.desk[2][0] == self.desk[2][1] == self.desk[2][2] and self.desk[2][0] != None:
      return True


  def vertical(self) -> Optional[bool]:
    """
    Evaluates vertical win
    """
    if self.desk[0][0] == self.desk[1][0] == self.desk[2][0] and self.desk[0][0] != None:
      return True
    if self.desk[0][1] == self.desk[1][1] == self.desk[2][1] and self.desk[0][1] != None:
      return True
    if self.desk[0][2] == self.desk[1][2] == self.desk[2][2] and self.desk[0][2] != None:
      return True


  def diagonal(self) -> Optional[bool]:
    """
    Evaluates diagonal win
    """
    if self.desk[0][0] == self.desk[1][1] == self.desk[2][2] and self.desk[0][0] != None:
      return True
    if self.desk[2][0] == self.desk[1][1] == self.desk[0][2] and self.desk[2][0] != None:
      return True


  def evaluate_win(self) -> Optional[bool]:
    """
    Method evaluates if someone wins
    """

    if self.horizontal() != None:
      return True
    if self.vertical() != None:
      return True
    if self.diagonal() != None:
      return True


  def evaluate_draw(self) -> bool:
    """
    Method evaluates if game ended up with draw
    """
    for row_i in range(len(self.desk)):
      for column_i in range(len(self.desk[0])):
        if self.desk[row_i][column_i] == None:
          return False

    return True


  def get_empty_positions(self) -> List:
    res = []
    for row_i in range(len(self.desk)):
      for column_i in range(len(self.desk[0])):
        if self.desk[row_i][column_i] == None:
          res.append((row_i, column_i))

    return res


