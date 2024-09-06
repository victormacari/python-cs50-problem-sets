i = input("Greeting: ")

words = i.split(" ");

if words[0] == "hello," or words[0] == "Hello," or i == "hello" or i == "Hello" :
    print("$0")
elif words[0][0] == "h" or words[0][0] == "H":
    print("$20")
else:
    print("$100")