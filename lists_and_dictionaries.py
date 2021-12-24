def main ():
    big_list = [
        {"name": "perro", "lastname": "gato"},
        {"name": "gato", "lastname": "perro"},
        {"name": "orrep", "lastname": "otag"},
        {"name": "otag", "lastname": "orrep"}
    ]

    big_dict = {
        "number": [1, 2, 3, 4, 5],
        "letters": ["a", "b", "c", "d", "e"],
        "symbols": ["!", "@", "#", "$", "%"]
    }


    for element in big_list:
        for key, value in element.items():
            print(f"{key}: {value}".center(20, " "))

    for key, array in big_dict.items():
        print(f"{key}:")

        for element in array:
            print(f"{element}".center(20, " "))

if __name__ == '__main__':
    main()