
'''
coinState = True

def flipCoin():
  global coinState
  if coinState == True:
    coinState = False
    return coinState
  elif coinState == False:
    coinState = True
    return coinState

flipCoin()

print(coinState)

print(flipCoin())
print(coinState)

'''
print("test line")

gameBoard = [[1,1,1],[1,1,1],[1,1,1]]

def showGameboard(gameBoard):
  print(gameBoard[0])
  print(gameBoard[1])
  print(gameBoard[2])

while gameBoard != [[0,0,0],[0,0,0],[0,0,0]]:
  showGameboard(gameBoard)

  playerChoice1 = int(input("choose coordinate 1: "))
  if playerChoice1 == 3:
    break  #this is just a simple out to quit the game whilst testing
  playerChoice2 = int(input("choose coordinate 2: "))

  if gameBoard[playerChoice1][playerChoice2] == 1:
    #gameBoard[playerChoice1][playerChoice2] = 0
    gameBoard[playerChoice1-1][playerChoice2] = 0 #this is a start, it doesnt fully work yet because it will sort of go out of bounds and then weirdly pick a wrong coordinate to change (probably a Python failsafe or something)
  else:
    gameBoard[playerChoice1][playerChoice2] = 1

#right now changing from heads/1 to tails/0 seems to sort of work (see comment above), I need to make sure the coins will also be turned back the right way (so tails will make more change to tails (I believe))
showGameboard(gameBoard)
