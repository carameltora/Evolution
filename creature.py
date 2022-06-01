import os # debug

'''
key:
m = move
c = check creature (returns bool)
l = location (returns bool)

action neurons:
m-up
m-down
m-left
m-right

sensory neurons:
c-up
c-down
c-left
c-right
c-radius
l-up
l-down
l-left
l-right
random

wiring:
positive/negative
determines neuron connections
'''

action_neurons = ["m-up","m-down","m-left","m-right"]

sensory_neurons = ["c-up","c-down","c-right","c-left","c-right","c-radius","l-up","l-down","l-left","l-right","random"]


def wire(s_neurons,a_neurons):
  a_neurons = a_neurons.copy()
  connections = {}
  for neuron in s_neurons:
    connections[neuron] = {random.choice([True,False]):a_neurons.pop(random.randint(0,len(a_neurons)-1))}
  return connections


def neurons():
  n = random.randint(2,4)
  return random.sample(sensory_neurons,n),random.sample(action_neurons,n)


def check(s_neuron,loc):
  if s_neuron == "c-up":
    if "■" in game_map.game_map[loc[1]-1][loc[0]]:
      return True
    else:
      return False
  elif s_neuron == "c-down":
    if "■" in game_map.game_map[loc[1]+1][loc[0]]:
      return True
    else:
      return False
  elif s_neuron == "c-left":
    if "■" in game_map.game_map[loc[1]][loc[0]-1]:
      return True
    else:
      return False
  elif s_neuron == "c-right":
    if "■" in game_map.game_map[loc[1]][loc[0]+1]:
      return True
    else:
      return False
  elif s_neuron == "c-radius": # make this actually work
    return random.choices([True,False],weights=[3,1])
  elif s_neuron == "l-up":
    if loc[1] > len(game_map.game_map):
      return True
    else:
      return False
  elif s_neuron == "l-down":
    if loc[1] < len(game_map.game_map):
      return True
    else:
      return False
  elif s_neuron == "l-left":
    if loc[0] < len(game_map.game_map[0]):
      return True
    else:
      return False
  elif s_neuron == "l-right":
    if loc[0] > len(game_map.game_map[0]):
      return True
    else:
      return False
  elif s_neuron == "random":
    return random.choice([True,False])


class Creature:
  def __init__(self,loc):
    self.loc = loc
    self.s_neurons, self.a_neurons = neurons()
    self.wiring = wire(self.s_neurons,self.a_neurons)
    self.cell = color.creature(self.wiring)
    game_map.game_map[loc[1]][loc[0]] = self.cell
  
  def move(self,movement): # make them collidable
    if movement == "m-down":
      if self.loc[1] < len(game_map.game_map) - 1 and game_map.game_map[self.loc[1]+1][self.loc[0]] == " ":
        game_map.game_map[self.loc[1]][self.loc[0]] = " "
        self.loc[1] += 1
        game_map.game_map[self.loc[1]][self.loc[0]] = self.cell
    elif movement == "m-up":
      if self.loc[1] > 0 and game_map.game_map[self.loc[1]-1][self.loc[0]] == " ":
        game_map.game_map[self.loc[1]][self.loc[0]] = " "
        self.loc[1] -= 1
        game_map.game_map[self.loc[1]][self.loc[0]] = self.cell
    elif movement == "m-left":
      if self.loc[0] > 0 and game_map.game_map[self.loc[1]][self.loc[0]-1] == " ":
        game_map.game_map[self.loc[1]][self.loc[0]] = " "
        self.loc[0] -= 1
        game_map.game_map[self.loc[1]][self.loc[0]] = self.cell
    elif movement == "m-right":
      if self.loc[0] < len(game_map.game_map[0]) - 1 and game_map.game_map[self.loc[1]][self.loc[0]+1] == " ":
        game_map.game_map[self.loc[1]][self.loc[0]] = " "
        self.loc[0] += 1
        game_map.game_map[self.loc[1]][self.loc[0]] = self.cell
  
  
  def update(self):
    for s_neuron, wiring in self.wiring.items():
      if check(s_neuron,self.loc) == list(wiring.keys())[0]:
        self.move(list(wiring.values())[0])

  def mutate(self):
    self.loc = [random.randint(1,58),random.randint(1,21)]
    self.s_neurons, self.a_neurons = neurons()
    self.wiring = wire(self.s_neurons,self.a_neurons)
    self.cell = color.creature(self.wiring)


generation = 0


def start():
  global creatures
  global generation
  for i in range(0,settings.gens + 1):
    generation = i
    for _ in range(70):
      time.sleep(0.1)
      for creature in creatures:
        try:
          creature.update()
        except IndexError:
          pass
    
    select()


def gen():
  _ = threading.Thread(target=start)
  _.daemon = True
  _.start()


def select(): # make customizable and randomly select
  global creatures
  
  add_creatures = []
  
  for creature in creatures: 
    if not settings.criteria(creature.loc):
      del creature
    else:
      if len(creatures) < 10:
        s = 3
      elif len(creatures) < 20:
        s = 4
      elif len(creatures) < 30:
        s = 5
      else:
        s = 7
      if random.randint(1,s) <= 3:
        for _ in range(random.choices([2,3],weights=[2,1])[0]):
          d_creature = deepcopy(creature)
          
          d_creature.loc = [random.randint(1,58),random.randint(1,21)]
          
          if random.randint(1,20) == 1:
            d_creature.mutate()
          
          add_creatures.append(d_creature)
  
  creatures.clear()
  
  for creature in add_creatures:
    creatures.append(creature)
  
  game_map.c()
  
  time.sleep(1.3)


creatures = [Creature([random.randint(1,58),random.randint(1,21)]) for _ in range(60)]
