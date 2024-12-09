print("Olá, seja bem vindo!\n")

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y 
    else:
        return "Erro: Divisão por zero não é permitida!"
    
def calculadora():
    print("Selecione a operaçao:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")

    while True:
        escolha = input("Digite o número da operação (1/2/3/4): ")

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, insira números válidos.")
                continue

            if escolha == '1':
                print(f"Resultado: {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {dividir(num1, num2)}")

            nova_operacao = input("Deseja realizar outra operação? (s/n): ")
            if nova_operacao.lower() != 's':
                print("Encerrando a calculadora. Até breve!")
                break
        else:
            print("Operação inválida, Tente novamente.")

calculadora()       