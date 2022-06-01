import time

import color

print("Hyper is cool\n")

time.sleep(0.1)
print(f"Press {color.txtc}[Enter]{color.reset}\n")

time.sleep(0.2)

input(f"This program is designed to {color.txtc}simulate evolution.{color.reset}\n")

time.sleep(0.2)

input(f"Each cell has it's own {color.txtc}neurons and connections{color.reset}, which lead\nto {color.txtc}diverse behaviors{color.reset}.\n")

time.sleep(0.2)

input(f"We will be simulating evolution by {color.txtc}selecting{color.reset} for\nthe cells that meet a {color.txtc}certain criteria{color.reset}.\n")

time.sleep(0.2)

input(f"If the program succeeds, the cells {color.txtc}should move towards{color.reset}\nthe {color.txtc}area you have selected{color.reset}, because that is the most {color.txtc}beneficial{color.reset}\narea for them to be in (They can reproduce)\n")

time.sleep(0.2)

choice = input(f"Choose your {color.txtc}selection{color.reset} criteria (Area that is 'good'):\n\n1: West Side\n2: East Side\n3: North Side\n4: South Side\n\n> ")

gens = int(input(f"\nHow many {color.txtc}generations{color.reset} would you like this to run?\n\n> "))

if choice == "1":
  def criteria(loc):
    if loc[0] > 20:
      return False
    else:
      return True

elif choice == "2":
  def criteria(loc):
    if loc[0] < 40:
      return False
    else:
      return True

elif choice == "3":
  def criteria(loc):
    if loc[1] > 10:
      return False
    else:
      return True

elif choice == "4":
  def criteria(loc):
    if loc[1] < 15:
      return False
    else:
      return True
