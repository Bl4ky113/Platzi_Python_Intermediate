def main():
    normal_list = [i for i in range(1, 21)]

    filter_list = list(filter(lambda element: element % 2 != 0, normal_list))

    print(normal_list, "\n", filter_list)

if __name__ == "__main__":
    main()