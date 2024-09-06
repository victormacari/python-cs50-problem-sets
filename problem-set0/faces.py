def main():
    i = input("What's the input? ")
    print(convert(i))


def convert(string: str) -> str:
    return string.replace(":)", "🙂").replace(":(", "☹️")

if __name__ == "__main__":
    main()