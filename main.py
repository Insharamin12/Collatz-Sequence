def collatz(number):  #function contains the main logic of the program
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

def main():
    try:
        user_input = int(input("Enter an integer: "))
        while user_input != 1:
            user_input = collatz(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
