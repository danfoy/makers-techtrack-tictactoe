# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!


def play_game(board_size):
  board = construct_board(board_size)
  player = "X"
  while not is_game_over(board):
    print(print_board(board))
    print(f"{slots_remaining(board)} goes left")
    print("It's " + player + "'s turn.")
    coords = request_coords(board)
    board = make_move(board, coords, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")


def construct_board(size):
  return [['.' for cell in range(size)] for row in range(size)]


def request_coords(board):
  row = int(input("Enter a row: "))
  column = int(input("Enter a column: "))
  if board[row][column] != '.':
    print(f"{row},{column} is taken! Choose another slot:")
    return request_coords(board)
  return [row, column]


def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid


def make_move(board, coords, player):
  x, y = coords
  board[x][y] = player
  return board


def get_cells(board, *coords):
  output = []
  for coord in coords:
    x, y = coord
    output.append(board[x][y])
  return output


# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, *coords):
  cells = get_cells(board, *coords)
  return "." not in cells


# This function will check if the group is all the same
def are_all_cells_the_same(board, *coords):
  cells = get_cells(board, *coords)
  entries = set(cells)
  return len(entries) == 1 and '.' not in entries


def winning_conditions(size):
  conditions = []
  # Rows
  for x in range(size):
    conditions.append([(x, y) for y in range(size)])
  
  # Columns
  for y in range(size):
    conditions.append([(x, y) for x in range(size)])
  
  # Diagonal 'backslash'
  conditions.append([(z, z) for z in range(size)])
  
  # Diagonal 'forward slash'
  conditions.append([(z, size - z -1) for z in range(size)])
  
  return conditions


def slots_remaining(board):
  count = 0
  for row in board:
    for cell in row:
      if cell == '.':
        count += 1
  return count


def is_game_over(board):
  if slots_remaining(board) == 0:
    return True
  # We go through our groups
  for group in winning_conditions(len(board)):
    # Skip uncompleted lines
    if is_group_complete(board, *[group[i] for i in range(len(board))]):
      if are_all_cells_the_same(board, *[group[i] for i in range(len(board))]):
        return True


board_size = int(input("Enter a board size: "))
print("Game time!")
play_game(board_size)
