
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
         countdown(i-1)

def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x -1)    

def main():
    i = int(input("What's i? "))
    print(countdown(i))
    print(fact(i))

if __name__ == "__main__":
    main()


