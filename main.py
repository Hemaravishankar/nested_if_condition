Height= int(input("enter your height: "))

if Height >= 120:
  print("u can ride the rollercaster")
  age = int(input("enter your age: "))
  if age < 12:
    print("Please pay 5$")
  elif age <= 18:
    print("Please pay 7$")
  else:
    print("Please pay 12$")
else:
  print("u can't ride it sorry")