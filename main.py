import random
import time
import creature
import game_map
import settings
import color


def clear():
  print("\033c", end = "")

creature.gen()

while True:
  time.sleep(0.4)
  clear()
  game_map.display()
  print("\n" + color.gen_color + "\tGeneration " + str(creature.generation))
