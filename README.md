# Resolução de Desafios em Python com GitHub Copilot e ChatGPT

Este repositório contém a resolução de diversos desafios de programação em Python. A proposta foi criar soluções utilizando conceitos básicos da linguagem, como manipulação de strings, operações matemáticas, condicionais e mais. As soluções foram desenvolvidas com o auxílio de ferramentas de IA, como GitHub Copilot e ChatGPT.

## Desafios Resolvidos

### 1. **Concatenando Dados 🐾**

**Descrição**: Solicitar dois dados do usuário e concatená-los em uma única string.

**Objetivo**: Praticar manipulação de strings, concatenando dois dados fornecidos pelo usuário.

**Código**:
```python
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatenar os dois dados
resultado = dado1 + " " + dado2

# Mostrar o resultado
print("Dados concatenados:", resultado)
```

---

### 2. **Repetindo Textos ✏️**

**Descrição**: Solicitar uma string e um número inteiro como entrada, e retornar a string repetida o número de vezes informado.

**Objetivo**: Praticar manipulação de strings e trabalhar com números inteiros para múltiplas repetições.

**Código**:
```python
texto = input("Digite o texto: ")
vezes = int(input("Quantas vezes você quer repetir o texto? "))

# Repetir o texto
resultado = texto * vezes

# Mostrar o resultado
print("Texto repetido:", resultado)
```

---

### 3. **Operações Matemáticas Simples 📐**

**Descrição**: Solicitar dois números e realizar uma operação simples entre eles (soma, subtração, multiplicação ou divisão).

**Objetivo**: Realizar operações matemáticas básicas com a entrada de dois números.

**Código**:
```python
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
```

---

### 4. **Verificando Números Pares e Ímpares 🧮**

**Descrição**: Receber um número inteiro e verificar se ele é par ou ímpar.

**Objetivo**: Trabalhar com condicionais (if/else) e operador módulo (`%`) para verificar a paridade de um número.

**Código**:
```python
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

---

### 5. **Calculando Média de Notas 📚**

**Descrição**: Solicitar três notas do usuário e calcular a média aritmética entre elas.

**Objetivo**: Aplicar operadores aritméticos para calcular a média e praticar a manipulação de entradas numéricas.

**Código**:
```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Mostrar a média
print(f"A média das notas é: {media:.2f}")
```

---

### 6. **Verificando Palíndromos 🔄**

**Descrição**: Testar se uma palavra é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).

**Objetivo**: Manipular strings e verificar se uma palavra é igual à sua versão invertida.

**Código**:
```python
palavra = input("Digite uma palavra: ")

# Inverter a palavra
palavra_invertida = palavra[::-1]

# Verificar se a palavra é um palíndromo
if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
```
