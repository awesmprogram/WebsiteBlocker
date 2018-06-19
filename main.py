def savemenu():
    code1 = raw_input("Put in your code now.")
    if code1 == "r1a1":
      print("Going to r1a1...")
      r1a1()
    if code1 == "r1a2":
      print("Going to r1a2...")
      r1a2()
    if code1 == "r1a3":
      print("Going to r1a3...")
      r1a3()
def r1a1():
  print("You can now say the following- Search the brown things, Search the blade. You can also always type Save and you put in a code. Your code is always shown after it says the things you could do. That will be how to save progress. Have fun!")
  print("Your code is r1a1")
  room1action1 = raw_input("What do you do? P.S....its case sensitive ")
  if room1action1 == "Search the brown things":
    print("You find a note on the tall one saying to chop this down. You also unlock the memory of trees and that the stub is a chopped tree trunk.")
    r1a2()
  if room1action1 == "Search the blade":
    print("As you examine it, you discover it to be a axe.")
    r1a2()  
  if room1action1 == "Save":
    savemenu()
  else:   
      r1a1()
def r1a2():
  print("You can now say the following- Search the brown   things, Search the blade")
  print("Your code is r1a2")
  room1action2 = raw_input("What do you do?")
  if room1action2 == "Search the brown things":
   print("You find a note on the tall one saying to chop this down. You also unlock the memory of trees and that the stub is a chopped tree trunk.")
   r1a3()
  if room1action2 == "Search the blade":
   print("As you examine it, you discover it to be a axe.")
   r1a3()
  if room1action2 == "Save":
    savemenu()
  else:
      r1a2()
def r1a3():
  print("You may now type Cut the tree")
  print("Your code is r1a3")
  room1action3 = raw_input("What do you do?")
  if room1action3 == "Save":
    savemenu()
  if room1action3 == "Cut the tree":
    yn1 = raw_input("Do you want to cut the tree? Type Yes or No.")
    if room1action3 == "Save":
      savemenu()
    if yn1 == "Yes":
      print("You cut the tree and it splits. As it falls the other direction, the elevator opens up. You walk in and wait to arrive at the next trial.")
      readycheck1 = raw_input("Click enter when you are ready.")
    if yn1 == "No":
      print("The floor opens from beneath you as you walk away. You fall into lava and die.")
      print("Game Over")
      print("You beat 0 shrines")
  else:
      r1a3()

r1a1()