def divisors (num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    
    return divisors

def main ():
    num = input("Enter a Number:  ")
    assert num.isnumeric() or int(num) >= 0, "Enter a Positive Number"
    print(divisors(int(num)))

if __name__ == "__main__":
    main()