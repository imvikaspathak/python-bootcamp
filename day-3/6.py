print("welcome treasure")
print("your mission to find the treasure")
a = input("Choose which direction you want to move - left or right or somewhere else: ")
aa=a.lower()

if(aa=="left"):
  b = input("Do you want to - swim or wait?:  \n")
  bb = b.lower()
  if(bb=="wait"):
    c = input("Which color door to choose - Red Blue Yellow or Anything else:  \n")
    cc = c.lower()
    if(cc=="red"):
      print("Burned By Fire.Game Over")
    elif(cc=="blue"):
      print("Eaten by Beasrs.Game Over")
    elif(cc=="yellow"):
      print("You Win")
    else:
      print("Wrong Door. Game Over")
  else:
    print("Attacked by trout.Game Over")
else:
  print("Fall into Hole. GameOver")