def main():
    dict = { i: round(i ** 0.5, 4) for i in range(1, 101) }

    print(dict)

if __name__ == '__main__':
    main()