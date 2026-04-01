valid = False
while not valid: #using nested while loop
  try:
      n=int(input("Enter a number: "))
      #enter a even or odd number
      while n%2==0: 

        print("bye") 
      valid = True 
  except ValueError:
    print("Invalid")  