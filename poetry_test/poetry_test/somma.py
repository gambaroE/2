def somma(num) -> None:
    ris=sum(num)
    return ris
def check(input):
        try:
            #divido l'input
            split_list=input.split(',')
            #lo metto a int
            int_list = [int(val) for val in split_list]
            #check che sia int
            if all(isinstance(val, int) for val in int_list):
                return int_list
            else:
                raise ValueError("La lista contiene valori non interi.")
        except ValueError:
            raise ValueError("Formato di input non valido. Fornisci una lista di interi separati da VIRGOLA.")



if __name__ == '__main__':
    #x = list(map(int, input("inserisci i valori da sommare separati da ,: ").split(',')))
    x = input("inserisci i valori da sommare separati da ,: ")
    checked=check(x)
    print("vuoi sommare questi numeri", checked)
    ris=somma(checked)
    print(f' Facile! fa {ris}')