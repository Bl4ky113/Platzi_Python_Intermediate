def main():
    dict = {i: i ** 3 for i in range(1, 101) if i % 3 != 0} 

    # for i in range(1, 101):
    #     if i % 3 != 0: 
    #         dict[i] = i ** 2
    
    print(dict)

if __name__ == '__main__':
    main()