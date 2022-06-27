
import random
import time
print("Welcome to the Adventure Game")
name = input ("What shall i call you Adventurer? ")
print("Hello ", name , ", It is an honour to have you on this journey")
time.sleep(2)
print("On this journey you are going to encounter some monsters. Each of them have certain weaknesses")
time.sleep(1)
print("You can fight them or avoid them, fight them only if you have certain elements") 
time.sleep(2)
print("if you are wise you will be able to complete the adventure if not then your journey will end")
time.sleep(2)

def new_func(options, random_number):
    computer_options = options[random_number]
    return computer_options

def new_func(user_strength):
    user_strength = [0]
    return user_strength 


while True:

 

 while True:
  user_input = input("Are you ready for your Adventure? Type Y/N ")
  time.sleep(1)

  if user_input.lower() == "n":
     print("We are sorry you couldn't join us for the adventure")
     exit()
  elif user_input.lower() == "y":
     print("Buckle up", name ,"we have a tough journey ahead")
     time.sleep(2)
     break
  else:
     print("Please give a valid answer")
     continue
 
 options = ["fire","water","air","earth"]
 random_number = random.randint(0,3)
 computer_options = options[random_number]
 user_strength = []

 while True:
  print("As you start your journey you are handed a box,The box contains one of the four elements. Air, Water, Fire, Earth")
  time.sleep(1)
  print("The elements will help you fight the monsters you meet in the journey")
  time.sleep(1)
  print("but be warned, not all elements work on every monster")
  time.sleep(1)
  q1_name = input ("Do you want to open the box? . Y/N  ")
  if q1_name.lower() == "n":
      print("Thats a brave move, i have to warn you though,you will not have an advantage which the box could have provided. And your journey will all depend on your luck")
      time.sleep(2)
      break
  if q1_name.lower() == "y":
   user_strength = [computer_options]
   print ("You found ", computer_options )
   if computer_options == "air":
       print("You have the power of Air, this element grants you the ability to manipulate it according to your liking")
   elif computer_options == "water":
       print("You have the power of Water, this element grants you the ability to manipulate it according to your liking")
   elif computer_options == "fire":
       print("You have the power of Fire, this element grants you the ability to manipulate it according to your liking")
   elif computer_options == "earth":
       print("You have the power of Earth, this element grants you the ability to manipulate it according to your liking")
  break

 time.sleep(2)
 print("As you go further into the forest you find an Ogre. Ogres weakness is one of the four elements, you can fight it if you have the element")
 time.sleep(2)
 
 while True:
   answer_1 = input("Do you want to avoid him or fight him.  Fight/Avoid  ")
   
   if answer_1.lower() == "fight" and computer_options == "fire":
    user_strength.append("earth")
    print("You were able to defeat the Ogre as fire is its weakness, you unlocked the earth element")
    break
   elif answer_1.lower() == "fight" and computer_options == "water":
    print(" You lose, You needed a Fire element to defeat it.")
    exit()
   elif answer_1.lower() == "fight" and computer_options == "air":
    print(" You lose, You needed a Fire element to defeat it.")
    exit()
   elif answer_1.lower() == "fight" and computer_options == "earth":
    print(" You lose, You needed a Fire element to defeat it.")
    exit()
   elif answer_1.lower() == "avoid":
    print("Thats a safe choice")
    break
   else:
     print("Please choose a valid options")
     continue
 time.sleep(2)
 print("The forest is dark and you are not alone")
 time.sleep(1)
 print("There is something lurking")
 time.sleep(2)
 print("It is the Riddler, and he has a riddle")
 time.sleep(2) 
  
 while True:
     while True:
      riddler_age = [30, 32,34,36,38,40,42,44,46,48,50]
      random_age = random.choice(riddler_age)
      random_age = int(random_age)
      print ("Riddler: 10 years ago, i was ", random_age ," and my sister was half my age. whats her age 5 years from now?")
      answer_2 = input(" Give your answer or Type Quit to end this level ")
      solution_riddler = ((random_age)/2)
      riddler_solution = solution_riddler + 15
      riddler_solution = int(riddler_solution)
      if answer_2.lower() == "quit":
          break
      if int (answer_2) == riddler_solution:
         user_strength.append ("intel")
         print("Riddler: You are correct, i grant you the power of Intel. This element is going to be helpful in your journey")
         break
      else:
         print("Riddler: You did not answer correctly, try again.")
         continue
     break
 time.sleep(2)
 print ("As you travel further, you find a river.")
 time.sleep(1)
 print ("you must cross the river, but there is large serpent in it")
 time.sleep(1)
 print ("You can use your luck in fighting the serpent or use Intel to evade it")
 time.sleep(1)
 print ("Intel is the power you get if you answered the riddler correctly")
 time.sleep(1)

 while True: 

    while True:
     answer_3 = input("Do you want to fight or evade, be warned without Intel it may be difficult to evade the serpent. ")
     luck = ["win","lose"]
     random_luck = random.randint(0,1)
     evade_luck = luck[random_luck]
     if answer_3.lower() == "fight" and "air" in user_strength:
        user_strength.append("water")
        print("With the power of Air, you succesfully defeated the serpent")
        time.sleep(1)
        print("You receaved the element of water")
        break
     elif answer_3.lower() == "evade" and "intel" in user_strength:
          print("With the help of Intel you were able to successfully cross the river")
          break
     elif answer_3.lower() == "evade" and evade_luck == "win":
          print("You are one lucky person, you were successfully able to cross the river without an Intel")
          break
     elif answer_3.lower() != "fight" or answer_3.lower() != "evade":
          print("Please choose a valid option")
          continue
     else:
         time.sleep(3)
         print("Sorry you don't have elements to cross this level, your journey ends here")
         time.sleep(3)
         exit()
    break
 print("After successfully crossing the river you reached a valley.")
 time.sleep(2)
 print("You are exhausted by the journey and you need energy")
 time.sleep(2)
 print("The valley has variety of wild fruits, some are poisonous and some are not")
 time.sleep(2)
 print("Do you have the knowledge of these fruits, be wise, a wrong fruit can end your journey right here")
 time.sleep(2)

 while True:
    while True:
     answer_4 = input("Do you want to eat a fruit from the valley, Y/N ")
     if answer_4.lower() == "y" and "earth" in user_strength:
         print("The element of Earth grants you the wisdom, You chose a good fruit")
         time.sleep(1)
         break
     elif answer_4.lower() == "n":
          print("Thats a safe choice but you still need energy to resume your journey")
          time.sleep(1)
          print("You can trade Intel or one of your Elements")
          time.sleep(1)
          print("you must have the element you are trading if you don't then you cannot continue your journey")
          time.sleep(1)
          user_trade = input("What do you want to trade? Intel, Fire, Water, Air or Earth? ")
          time.sleep(1)
          if user_trade.lower() == "intel":
             user_strength.remove("intel")
             print("You used your intel to gain energy")
             time.sleep(1)
             print("you have successfully passed the valley")
             time.sleep(1)
             break
          elif user_trade.lower() == "air":
               user_strength.remove("air")
               print("You used air element to gain energy")
               time.sleep(1)
               print("you have successfully passed the valley")
               time.sleep(1)
               break
          elif user_trade.lower() == "water":
               user_strength.remove("water")
               print("You used water element to gain energy")
               time.sleep(1)
               print("you have successfully passed the valley")
               time.sleep(1)
               break
          elif user_trade.lower() == "fire":
               user_strength.remove("fire")
               print("You used fire element to gain energy")
               time.sleep(1)
               print("you have successfully passed the valley")
               time.sleep(1)
               break
          elif user_trade.lower() == "earth":
               print("You don't need to trade Earth element, it helps you in identifying the fruits")
               time.sleep(1)
               print("you have successfully passed the valley")
               time.sleep(1)
               break
     else:
         print("Choose a valid option")
         time.sleep(1)
         quit
    break
 print("As you travel further you reach a lava mountain")
 time.sleep(1)
 print("In that lava mountain resides a Fire breathing Dragon")
 time.sleep(1)
 print("You need one of the element to defeat the dragon")
 time.sleep(1)
 print("You currently have these elements",  user_strength )
 time.sleep(1)
 print("This time you have to fight the Dragon, you cannot avoid it")
 while True: 
   if "intel" in user_strength :
     print("You have the element of Intel, this can be helpful in fighting the Dragon")
     time.sleep(1)
     trade_intel = input("Trade your intel for the element you think can beat the dragon: Air, Water, Fire, Earth ").lower()
     trade_intel = str(trade_intel)
     if trade_intel != "air" and trade_intel != "water" and trade_intel != "earth" and trade_intel != "fire" :
         print("Please choose a valid option")
         continue
     else:
         user_strength.append(trade_intel)
         user_strength.remove("intel")
         break
   break
 while True:
     answer_5 = input("what element would you like to use against the dragon? ").lower()
     if answer_5 == "water" and "water" in user_strength:
         time.sleep(1)
         print("With the element of water you were able to defeat the Dragon")
         time.sleep(1)
         print("You have gained the element of Fire")
         if "fire" not in user_strength:
             user_strength.append("fire")
             break
         else:
             break
     elif answer_5 == "water" and "water" not in user_strength:
         user_luck = ["win","lose"]
         user_fate = random.randint(0,1)
         fate_user = user_luck[user_fate]
         if fate_user == "win":
             time.sleep(2)
             user_strength.append("luck")
             print("You are one Lucky man, you defeated the dragon with just your luck")
             print("You have acquired the rarest element: Luck")
             break
         else:
             time.sleep(2)
             print("You don't have water element, therefore you couldn't defeat the dragon")
             time.sleep(1)
             print("Your journey ends here")
             exit()
     else:
         print("The Dragon could only be defeated by Water")
         time.sleep(1)
         print("Your journey ends here")
         exit()
 print("You have reached the end of the journey but before you finish")
 time.sleep(1)
 print("The Riddler has another riddle for you")
 time.sleep(2)
 print("This thing all things devours; Birds,beasts,trees,flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats mountain down")
 answer_6 = input("What is it? ").lower()
 if answer_6 == "time":
     print("You are a Genius")
     time.sleep(1)
     print("And as a reward i grant you the missing elements")
     if "fire" not in user_strength:
         user_strength.append("fire")
     elif "water" not in user_strength:
          user_strength.append("water")
     elif "earth" not in user_strength:
          user_strength.append("earth")
     elif "air" not in user_strength:
          user_strength.append("air")
          break
     break
 else:
     print("Sorry you got it wrong")
     break        
time.sleep(2)
print("You have these elements ", user_strength)
if "earth" in user_strength and "water" in user_strength and "air" in user_strength and "fire" in user_strength :
   time.sleep(1)
   print("Congratulations you have successfully completed the adventure")
else:
    print("You successfully completed the journey but could not gather all the elements")
exit()

