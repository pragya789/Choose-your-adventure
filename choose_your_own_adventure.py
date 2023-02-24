name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and "
               "you can go left or right. Which way you would like to go? ").lower()

if answer == "left":
     answer = input("You come to a river, You can walk around or swim accross? Type walk to walk around and swim to swim across: ")

     if answer == "swim":
         print("You swam across and were eaten by an alligator.")
     elif answer == "walk" :
         print("You walked for many miles, ran out of water and you lost the game.")
     else:
         print("Not a valid option. You lose.")

elif answer == "right":
     answer = input("You come to a bridge, it looks wooby, do you want to cross or go back: ")

     if answer == "back":
         print("You go back and lose")
     elif answer == "cross":
         answer = input("You cross the bridge and meet a stranger. Do you talk to them(yes/no)? ")
         if answer == "yes":
             print("You talked to the stranger, they gave you gold. You won!")
         elif answer == "no":
             print("You ignore the stranger and they are affended by you. You lose.")

         else:
             print("Not a valid option. You lose")

     else:
         print("Not a valid option. You lose.")
else:
     print("Not a valid option. You lose.")
print("Thank you for your time",name )