def main():
    normal_list = [i for i in range(1, 11)]

    map_list = list(map(lambda element: element ** 2, normal_list))

    print(normal_list)
    print(map_list)

if __name__ == "__main__":
    main()