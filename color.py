import random

gen_color = "\033[0;94m"
txtc = "\033[0;94m"
reset = "\033[0m"


sensory_neurons = ["c-up","c-down","c-right","c-left","c-right","c-radius","l-up","l-down","l-left","l-right","random"]
action_neurons = ["m-up","m-down","m-left","m-right"]


def rgb(fg=(255,255,255),bg=None):
  try:
    return f"\033[38;2;{fg[0]};{fg[1]};{fg[2]};48;2;{bg[0]};{bg[1]};{bg[2]}m"
  except:
    return f"\033[38;2;{fg[0]};{fg[1]};{fg[2]}m"


def creature(wiring):
  for sensor, conn in wiring.items():
    g = sensory_neurons.index(sensor) * 14 + len(str(wiring.keys())) * 14
    b = len(str(sensor)) * 17 + len(str(wiring.items())) * 14
    r = (len(str(sensor)) + len(str(conn)*2)) * 16
  
  return rgb(fg=(r+20,g+20,b+20)) + "■"
