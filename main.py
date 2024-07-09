def calc_ihh(total, array_data):
    ihh = 0
    for data in array_data:
        ihh += pow((data/total), 2)

    print(ihh)


def main():
    array_data = []
    total = 0
    response = input("Existe total mundial (1: sim, 0: nao)")
    if response == '1':
        total = int(input("Diz-me o total: "))
    while True:
        data = int(input("Escreve o dado numero {}: ".format(len(array_data))))
        if data == 0:
            if response == '0':
                total = sum(array_data)

            calc_ihh(total, array_data)
            break
        array_data.append(data)


if __name__ == "__main__":
    main()
