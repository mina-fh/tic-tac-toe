def main():
  tt = TicTacToe()
  player = 1
  for i in range(9):
    tt.display()
    tt.input(player)
    comp = tt.compCheck(player)
    if comp == True:
      break
    player *= (-1)
        
  tt.display()
  if comp == True:
    print("■ ■" + tt.mark[player] + "is the Winner！■ ■")
  else:
    print("■ ■ It's a Draw！ ■ ■")
  input("Exit")


class TicTacToe:
  def __init__(self):
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.mark = {1: "〇", 0:"　", -1: "✕"}

  def input(self, player):
    while True:
      print("\n" + self.mark[player] + "'s Turn")
      xy = self.comInput()
      if self.board[xy[1]][xy[0]] == 0:
        self.board[xy[1]][xy[0]] = player
        break
      print("This cell is already filled.")


  def comInput(self):
    x = -1
    y = -1
    while ((y < 0) or (y > 2)):
      try: 
        y = int(input("Row(0~2): "))
      except:
        print("Input value is invalid.！")
    while ((x < 0) or (x > 2)):
      try:
        x = int(input("Column(0~2): "))
      except:
        print("Input value is invalid.")
    return [x, y]
        
  def display(self):
    print("　　０　１　２")
    self.dispSub(0)
    print("　　ー＋ー＋ー")
    self.dispSub(1)
    print("　　ー＋ー＋ー")
    self.dispSub(2)

  def compCheck(self, player):
    win = None
    num = len(self.board)

    # checking rows
    # i = row, j = column
    for i in range(num):
      win = True
      for j in range(num):
        if self.board[i][j] != player:
          win = False
          break
      if win:
        return win

    # checking columns
    for i in range(num):
      win = True
      for j in range(num):
        if self.board[j][i] != player:
          win = False
          break
      if win:
        return win

    # checking diagonals
    win = True
    for i in range(num):
      if self.board[i][i] != player:
        win = False
        break
    if win:
      return win

    win = True
    for i in range(num):
      if self.board[i][num - 1 - i] != player:
        win = False
        break
    if win:
      return win
    return False

  def dispSub(self, y):
    print(str(y) + "　" + self.mark[self.board[y][0]] + " | " + \
          self.mark[self.board[y][1]] + " | " + self.mark[self.board[y][2]])

if __name__ == "__main__":
  main()
