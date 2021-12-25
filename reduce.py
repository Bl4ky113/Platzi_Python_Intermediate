from functools import reduce

def main():
    normal_list = [2 for i in range(1, 6)]

    reduce_number = reduce(lambda a, b: a * b, normal_list)

    print(normal_list) 
    print(reduce_number) 

if __name__ == "__main__":
    main()