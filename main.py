maze = [["X", " ", "X", "X", "X", "X", "X", "X", "X","X"],
        ["X", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
        ["X", " ", "X", "X", "X", "X", "X", "X", " ", "X"],
        ["X", " ", "X", " ", " ", " ", "X", " ", " ", "X"],
        ["X", " ", "X", " ", "X", " ", "X", "X", " ", "X"],
        ["X", " ", "X", " ", "X", " ", "X", " ", " ", "X"],
        ["X", " ", " ", " ", "X", " ", " ", "X", " ", "X"],
        ["X", "X", "X", "X", "X", "X", " ", "X", "X", "X"]]

#prints maze 
def drawMaze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end='')
        print()

#Rows are 0-7
#Columns are 0-9
drawMaze()

import random

#checks if the spot the bot is moving to is empty (is not an X)
def checkForX(r,c):
  if (maze[r][c] != "X"):
    position = "empty"
  else:
    position = "not empty"
  return position


#move bot one row up
def moveUp(r):
  #if bot's row position is greater than zero (top row), it can move one row up
  if r > 0:
    r = r - 1
    
  return r  

#move bot one row down
def moveDown(r):
  #if bot's row position is less than eight (bottom row), it can move one row down
  if r < 8:
    r = r + 1

  return r


#move bot one column left
def moveLeft(c):
  #if bot's column position is greater than zero (farthest left column), it can move one column left
  if c > 0:
    c = c - 1

  return c

#move bot one column right
def moveRight(c):
  #if bot's column position is less than nine (farthest right column), it can move one column right
  if c < 9:
    c = c + 1

  return c


#put bot in starting position
r = 0
c = 1
#sets the counter to start at 1
count = 1

print()
print("------------------------------")
print()

#put O at the starting position and print maze
maze[r][c] = "O"
drawMaze()

#moving the bot up, down, left, or right into empty positions until it exits the maze
while maze[7][6] != "O":
  #use random function to generate a random move
  randNum = random.randint(1,4)

  #random move 1 is up
  if randNum == 1:
    r = moveUp(r)
    #checks if new position is empty
    position = checkForX(r, c)
    if position == "empty":
      #plot O in new position
      maze[r][c] = "O"
      #removes the O from the old position
      maze[r+1][c] = " " 
      #adds 1 to the move counter
      count = count + 1
      #prints new maze along with divider
      drawMaze()  
      print()
      print("------------------------------")
      print()
    else:
      #if the new position is not empty, the o will remain in the old position and the maze will not be printed because this is not a move. This is done to by reseting the original row position.
      r = r + 1

  #random move 2 is down
  elif randNum == 2:
    r = moveDown(r)
    #checks if new position is empty
    position = checkForX(r, c)
    if position == "empty":
      #plot O in new position
      maze[r][c] = "O"
      #removes the O from the old position
      maze[r-1][c] = " " 
      #adds 1 to the move counter
      count = count + 1
      #prints new maze along with divider
      drawMaze()
      print()
      print("------------------------------")
      print()
    else:
      #if the new position is not empty, the o will remain in the old position and the maze will not be printed because this is not a move. This is done to by reseting the original row position.
      r = r - 1

  #random move 3 is left
  elif randNum == 3:
    c = moveLeft(c)
    #checks if new position is empty
    position = checkForX(r, c)
    if position == "empty":
      #plot O in new position
      maze[r][c] = "O"
      #removes the O from the old position
      maze[r][c+1] = " " 
      #adds 1 to the move counter
      count = count + 1
      #prints new maze along with divider
      drawMaze()
      print()
      print("------------------------------")
      print()
    else:
       #if the new position is not empty, the o will remain in the old position and the maze will not be printed because this is not a move. This is done to by reseting the original column position.
      c = c + 1

  #random move 4 is right
  elif randNum == 4:
    c = moveRight(c)
    #checks if new position is empty
    position = checkForX(r, c)
    if position == "empty":
      #plot O in new position
      maze[r][c] = "O"
      #removes the O from the old position
      maze[r][c-1] = " " 
      #adds 1 to the move counter
      count = count + 1
      #prints new maze along with divider
      drawMaze()
      print()
      print("------------------------------")
      print()
    else:
      #if the new position is not empty, the o will remain in the old position and the maze will not be printed because this is not a move. This is done to by reseting the original column position.
      c = c - 1
print("Maze Completed")
print("Number of Bot Moves: " + str(count))