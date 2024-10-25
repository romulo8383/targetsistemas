

def main():
    fibonacci = 0
    aux = 1
    atual = 0
    numero = int(input("Digite um numero:"))
    print(fibonacci, end=", ")                 # acrescenta o 0 na sequencia fibonacci
    
    for i in range(numero):
        atual = fibonacci
        fibonacci = fibonacci + aux
        aux = atual
        if fibonacci < numero:
            print(fibonacci, end=", ")        # mantem elementos na mesma linha
        elif fibonacci == numero:
            print(fibonacci, end=", ")
            print(f"O numero {numero} pertence a sequencia Fibonacci")
            break                             # para o loop por ja ter a resposta
        elif fibonacci > numero:
            print(fibonacci, end=", ")
            print(f"O numero {numero} nao pertence a sequencia Fibonacci")
            break ;


if __name__ == '__main__' :

    main()

    