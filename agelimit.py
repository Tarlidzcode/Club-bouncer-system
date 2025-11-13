val = input("Enter your age: ")
print(val )

try:
    nm= int(val)
    if nm < 18:
      print("Go home young one")
    
    if nm <21:
        print("Come on in but you know you cant drink right")
    
    elif nm >= 21:
        print("welcome!!!")
    
except ValueError:
    print("please enter a valid number")
