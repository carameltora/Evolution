
def display():
  global game_map
  print("\n".join(["".join(l) for l in game_map]))

def c():
  global game_map
  game_map = [[i] * 60 for i in list([" "] * 23)]
