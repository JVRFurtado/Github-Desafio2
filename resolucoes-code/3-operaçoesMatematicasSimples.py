# Solicitar dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicitar a operação que o usuário deseja realizar
print("Escolha a operação:")
print("1. Soma (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

operacao = input("Digite o número da operação (1/2/3/4): ")

# Realizar a operação escolhida
if operacao == "1":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "2":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "3":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro! Divisão por zero não permitida.")
else:
    print("Operação inválida! Escolha um número entre 1 e 4.")
