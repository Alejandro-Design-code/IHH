

def calc_ihh(total, array_data):
    ihh = 0
    for data in array_data:
        ihh += pow((data/total), 2)

    print(ihh)


def main():
    array_data = []
    while True:
        data = int(input(f"Escreve o dado numero {len(array_data)}: "))
        if data == 0:
            total = sum(array_data)
            calc_ihh(total, array_data)
            break

        array_data.append(data)
        

if __name__ == "__main__":
    main()
