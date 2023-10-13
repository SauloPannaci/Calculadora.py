
def somar(numero, memoria):
    return numero + memoria

def subtrair(numero, memoria):
    return memoria - numero

def multiplicar(numero, memoria):
    return numero * memoria

def dividir(numero, memoria):
    if numero != 0:
        return memoria / numero
    else:
        return "Erro: Divisão por zero"

def limpar_memoria():
    return 0

def calculadora():
    memoria = 0

    while True:
        print(f"Memória atual: {memoria}")
        print("Opções:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Limpar Memória")
        print("6. Sair")

        opcao = input("Escolha uma opção (1/2/3/4/5/6): ")

        if opcao == "1":
            numero = float(input("Digite o número a ser somado: "))
            memoria = somar(numero, memoria)
        elif opcao == "2":
            numero = float(input("Digite o número a ser subtraído: "))
            memoria = subtrair(numero, memoria)
        elif opcao == "3":
            numero = float(input("Digite o número a ser multiplicado: "))
            memoria = multiplicar(numero, memoria)
        elif opcao == "4":
            numero = float(input("Digite o número a ser dividido: "))
            resultado = dividir(numero, memoria)
            if isinstance(resultado, str):
                print(resultado)
            else:
                memoria = resultado
        elif opcao == "5":
            memoria = limpar_memoria()
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

calculadora()