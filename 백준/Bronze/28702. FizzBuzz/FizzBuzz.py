def main():
    arr = []
    for _ in range(3):
        arr.append(input())

    index = None
    for word in arr:
        if word.isdigit():
            index = arr.index(word)
    number = None
    if index == 0:
        number = int(arr[index]) + 3
    elif index == 1:
        number = int(arr[index]) + 2
    else:
        number = int(arr[index]) + 1

    fizzbuzz(number)


def fizzbuzz(num):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0 and num % 5 != 0:
        print('Fizz')
    elif num % 3 != 0 and num % 5 == 0:
        print('Buzz')
    else:
        print(num)

if __name__ == "__main__":
    main()