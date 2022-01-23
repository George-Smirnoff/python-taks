def max_binary_gap(number: int) -> int:
    binary = convert_to_binary(number)
    print(f"The binary value: {binary}")

    counter = 0
    max_gap = 0
    for i in binary:
        i = int(i)
        if i == 1:
            if counter > max_gap:
                max_gap = counter
            counter = 0
        elif i == 0:
            counter+=1
        else:
            print("Unexpected value in binary representation!")
    return max_gap


def convert_to_binary(number: int) -> str:
    return format(number, "b")


def main():
    try:
        print("Inter your number to calculate binary gap:")
        number = int(input())
    except Exception as e:
        print(e)
    result = max_binary_gap(number)
    print(result)
    

if __name__ == "__main__":
    main()