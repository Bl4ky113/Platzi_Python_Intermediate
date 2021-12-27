file_path = {
    "numbers": "./files/numbers.txt",
    "names": "./files/names.txt",
}

def read():
    number_list = []
    with open(file_path["numbers"], "r", encoding="UTF-8") as file:
        for line in file:
             number_list.append(int(line))

    print(number_list)

def write():
    names = ["Martín", "Kitty", "Perro", "Gato"]
    with open(file_path["names"], "w+", encoding="UTF-8") as file:
        for name in names:
            file.write(name)
            file.write("\n")

        print(file)

def main():
    read()
    write()

if __name__ == "__main__":
    main()